<template>
  <div class="admin-page">
    <!-- 登录界面 -->
    <AdminLogin v-if="!authenticated" @login-success="onLoginSuccess" />

    <!-- 管理界面 -->
    <div v-else class="admin-container">
      <header class="admin-header">
        <h1>Vehicle Management</h1>
        <div class="header-actions">
          <button class="btn-add" @click="openAddForm">+ Add Vehicle</button>
          <button class="btn-deploy" @click="handleDeploy" :disabled="deploying">
            {{ deploying ? 'Deploying...' : 'Deploy to Live Site' }}
          </button>
          <button class="btn-logout" @click="handleLogout">Logout</button>
        </div>
      </header>

      <!-- 状态提示 -->
      <div v-if="statusMsg" class="status-bar" :class="statusType">
        {{ statusMsg }}
      </div>

      <!-- 车辆列表 -->
      <VehicleTable
        v-if="!showForm"
        :vehicles="vehicles"
        :listLoading="listLoading"
        @refresh="loadVehicles"
        @edit="openEditForm"
        @delete="confirmDelete"
        @toggle-enabled="toggleEnabled"
      />

      <!-- 新增/编辑表单 -->
      <VehicleForm
        v-if="showForm"
        ref="vehicleFormRef"
        :isEditing="isEditing"
        :brandsData="brandsData"
        :brandsLoading="brandsLoading"
        :saving="saving"
        @save="handleFormSave"
        @cancel="cancelForm"
      />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { getFileContent, updateFile, uploadImage, deployToMain } from '@/utils/github.js'
import AdminLogin from '@/components/admin/AdminLogin.vue'
import VehicleTable from '@/components/admin/VehicleTable.vue'
import VehicleForm from '@/components/admin/VehicleForm.vue'

// 认证状态
const authenticated = ref(false)
let token = ''

// 车辆数据
const vehicles = ref([])
const listLoading = ref(false)
const vehiclesFileSha = ref('')

// 表单状态
const showForm = ref(false)
const isEditing = ref(false)
const editingId = ref(null)
const saving = ref(false)
const deploying = ref(false)
const vehicleFormRef = ref(null)

// 状态提示
const statusMsg = ref('')
const statusType = ref('info')

// 品牌数据库
const brandsData = ref([])
const brandsLoading = ref(false)

function showStatus(msg, type = 'info') {
  statusMsg.value = msg
  statusType.value = type
  setTimeout(() => { statusMsg.value = '' }, 5000)
}

// 登录成功回调
function onLoginSuccess(t) {
  token = t
  authenticated.value = true
  sessionStorage.setItem('gh_token', token)
  loadVehicles()
  loadBrandsData()
}

function handleLogout() {
  authenticated.value = false
  token = ''
  sessionStorage.removeItem('gh_token')
  vehicles.value = []
}

// 加载车辆数据
async function loadVehicles() {
  listLoading.value = true
  try {
    const { content, sha } = await getFileContent(token, 'public/data/vehicles.json')
    vehicles.value = JSON.parse(content)
    vehiclesFileSha.value = sha
  } catch (err) {
    showStatus('Failed to load vehicles: ' + err.message, 'error')
  } finally {
    listLoading.value = false
  }
}

// 加载品牌数据库
async function loadBrandsData() {
  brandsLoading.value = true
  try {
    const url = 'https://raw.githubusercontent.com/OUTshipping/OUTshipping.github.io/source/public/data/brands.json'
    const resp = await fetch(url)
    if (resp.ok) {
      const data = await resp.json()
      brandsData.value = data.brands || []
    }
  } catch (err) {
    console.warn('Failed to load brands database:', err)
  } finally {
    brandsLoading.value = false
  }
}

// 切换启用/禁用
async function toggleEnabled(vehicle) {
  vehicle.enabled = !vehicle.enabled
  await saveAllVehicles('Toggle vehicle: ' + vehicle.name)
}

// 打开新增表单
function openAddForm() {
  isEditing.value = false
  editingId.value = null
  showForm.value = true
  // 等组件渲染后重置
  setTimeout(() => {
    vehicleFormRef.value?.resetForm(null)
  })
}

// 打开编辑表单
function openEditForm(vehicle) {
  isEditing.value = true
  editingId.value = vehicle.id
  showForm.value = true
  setTimeout(() => {
    vehicleFormRef.value?.resetForm({
      name: vehicle.name, slug: vehicle.slug, type: vehicle.type,
      range: vehicle.range, seats: vehicle.seats,
      configuration: vehicle.configuration, description: vehicle.description,
      coverImage: vehicle.coverImage, colors: [...vehicle.colors],
      specs: { ...vehicle.specs }, detailImages: [...vehicle.detailImages]
    })
  })
}

function cancelForm() { showForm.value = false }

// 将文件转 Base64（不含前缀）
function fileToBase64(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader()
    reader.onload = () => { resolve(reader.result.split(',')[1]) }
    reader.onerror = reject
    reader.readAsDataURL(file)
  })
}

// 确认删除
async function confirmDelete(vehicle) {
  if (!confirm(`Are you sure you want to delete "${vehicle.name}"?`)) return
  vehicles.value = vehicles.value.filter(v => v.id !== vehicle.id)
  await saveAllVehicles('Delete vehicle: ' + vehicle.name)
}

// 保存所有车辆数据到 GitHub（含 SHA 不匹配自动重试）
async function saveAllVehicles(commitMsg) {
  try {
    const content = JSON.stringify(vehicles.value, null, 2)
    const result = await updateFile(token, 'public/data/vehicles.json', content, vehiclesFileSha.value, commitMsg)
    vehiclesFileSha.value = result.content.sha
    showStatus('Saved successfully! Site will update in 1-2 minutes.', 'success')
  } catch (err) {
    if (err.message && err.message.includes('does not match')) {
      try {
        showStatus('SHA mismatch, retrying...', 'info')
        const { sha: latestSha } = await getFileContent(token, 'public/data/vehicles.json')
        vehiclesFileSha.value = latestSha
        const content = JSON.stringify(vehicles.value, null, 2)
        const result = await updateFile(token, 'public/data/vehicles.json', content, vehiclesFileSha.value, commitMsg)
        vehiclesFileSha.value = result.content.sha
        showStatus('Saved successfully! Site will update in 1-2 minutes.', 'success')
      } catch (retryErr) {
        showStatus('Save failed after retry: ' + retryErr.message, 'error')
      }
    } else {
      showStatus('Save failed: ' + err.message, 'error')
    }
  }
}

// 一键部署
async function handleDeploy() {
  if (!confirm('确认将当前数据部署到前台网站？')) return
  deploying.value = true
  try {
    await deployToMain(token)
    showStatus('Deployed successfully! Live site will update in ~1 minute.', 'success')
  } catch (err) {
    showStatus('Deploy failed: ' + err.message, 'error')
  } finally {
    deploying.value = false
  }
}

// 表单保存回调（从 VehicleForm 组件接收数据）
async function handleFormSave({ formData, pendingCoverFile, pendingDetailFiles }) {
  saving.value = true
  try {
    const slug = formData.slug
    // 上传封面图
    if (pendingCoverFile) {
      const ext = pendingCoverFile.name.split('.').pop()
      const coverPath = `public/vehicles/${slug}/cover.${ext}`
      const b64 = await fileToBase64(pendingCoverFile)
      await uploadImage(token, coverPath, b64, `Upload cover for ${formData.name}`)
      formData.coverImage = `/vehicles/${slug}/cover.${ext}`
    }

    // 上传详情图
    const existingCount = formData.detailImages.length - pendingDetailFiles.length
    for (let i = 0; i < pendingDetailFiles.length; i++) {
      const file = pendingDetailFiles[i]
      const ext = file.name.split('.').pop()
      const imgPath = `public/vehicles/${slug}/${existingCount + i + 1}.${ext}`
      const b64 = await fileToBase64(file)
      await uploadImage(token, imgPath, b64, `Upload image for ${formData.name}`)
      formData.detailImages[existingCount + i] = `/vehicles/${slug}/${existingCount + i + 1}.${ext}`
    }

    // 构建车辆对象
    const vehicleData = {
      id: isEditing.value ? editingId.value : (Math.max(0, ...vehicles.value.map(v => v.id)) + 1),
      slug: formData.slug, enabled: true,
      name: formData.name, type: formData.type,
      range: formData.range, seats: formData.seats,
      configuration: formData.configuration,
      coverImage: formData.coverImage,
      colors: formData.colors,
      description: formData.description,
      specs: formData.specs,
      detailImages: formData.detailImages
    }

    if (isEditing.value) {
      const idx = vehicles.value.findIndex(v => v.id === editingId.value)
      if (idx !== -1) {
        vehicleData.enabled = vehicles.value[idx].enabled
        vehicles.value[idx] = vehicleData
      }
    } else {
      vehicles.value.push(vehicleData)
    }

    await saveAllVehicles(isEditing.value ? `Update vehicle: ${formData.name}` : `Add vehicle: ${formData.name}`)
    showForm.value = false
  } catch (err) {
    showStatus('Save failed: ' + err.message, 'error')
  } finally {
    saving.value = false
  }
}

onMounted(() => {
  const savedToken = sessionStorage.getItem('gh_token')
  if (savedToken) {
    token = savedToken
    authenticated.value = true
    loadVehicles()
    loadBrandsData()
  }
})
</script>


<style scoped>
.admin-page {
  min-height: 100vh;
  background: var(--secondary-color);
  color: var(--primary-color);
}

/* 管理界面 */
.admin-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 1.5rem;
}

.admin-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.25rem 1.5rem;
  background: var(--primary-color);
  border-radius: 0.75rem;
  margin-bottom: 1.5rem;
  box-shadow: var(--shadow);
}

.admin-header h1 {
  color: white;
  margin: 0;
  font-size: 1.5rem;
  font-weight: 700;
}

.header-actions {
  display: flex;
  gap: 0.625rem;
}

.btn-add {
  background: #10b981; color: #fff; border: none;
  padding: 0.625rem 1.25rem; border-radius: 9999px;
  font-weight: 600; cursor: pointer; transition: all 0.2s;
  font-family: inherit; min-height: 44px; font-size: 0.875rem;
}
.btn-add:hover { background: #059669; transform: translateY(-1px); }

.btn-deploy {
  background: var(--accent-color); color: #fff; border: none;
  padding: 0.625rem 1.25rem; border-radius: 9999px;
  font-weight: 600; cursor: pointer; transition: all 0.2s;
  font-family: inherit; min-height: 44px; font-size: 0.875rem;
}
.btn-deploy:hover { background: var(--accent-color-dark); transform: translateY(-1px); }
.btn-deploy:disabled { background: #94a3b8; cursor: not-allowed; transform: none; }

.btn-logout {
  background: transparent; color: #fff;
  border: 1px solid rgba(255, 255, 255, 0.3);
  padding: 0.625rem 1.25rem; border-radius: 9999px;
  font-weight: 600; cursor: pointer; transition: all 0.2s;
  font-family: inherit; min-height: 44px; font-size: 0.875rem;
}
.btn-logout:hover { background: rgba(255, 255, 255, 0.1); border-color: rgba(255, 255, 255, 0.5); }

/* 状态条 */
.status-bar {
  padding: 0.875rem 1.25rem; border-radius: 0.75rem;
  margin-bottom: 1.5rem; font-weight: 600; font-size: 0.875rem;
  border-left: 4px solid transparent;
}
.status-bar.success { background: #ecfdf5; color: #065f46; border-left-color: #10b981; }
.status-bar.error { background: #fef2f2; color: #991b1b; border-left-color: #ef4444; }
.status-bar.info { background: #eff6ff; color: #1e40af; border-left-color: var(--accent-color); }

@media (max-width: 768px) {
  .admin-container { padding: 1rem; }
  .admin-header { flex-direction: column; gap: 1rem; text-align: center; padding: 1rem; }
  .admin-header h1 { font-size: 1.25rem; }
  .header-actions { flex-wrap: wrap; justify-content: center; width: 100%; }
  .header-actions button { flex: 1; min-width: 120px; }
}

@media (max-width: 480px) {
  .admin-container { padding: 0.75rem; }
  .admin-header { border-radius: 0.5rem; padding: 0.875rem; }
  .admin-header h1 { font-size: 1.1rem; }
  .header-actions button { font-size: 0.8rem; padding: 0.5rem 1rem; }
}
</style>
