<template>
  <div class="admin-page">
    <!-- 登录界面 -->
    <div v-if="!authenticated" class="login-container">
      <div class="login-card">
        <h1>TG Automobile Admin</h1>
        <p class="login-desc">Enter your GitHub Personal Access Token to manage vehicles.</p>
        <div class="login-form">
          <input
            v-model="tokenInput"
            type="password"
            placeholder="GitHub Personal Access Token"
            @keyup.enter="handleLogin"
          />
          <button @click="handleLogin" :disabled="loginLoading">
            {{ loginLoading ? 'Verifying...' : 'Login' }}
          </button>
          <p v-if="loginError" class="error-msg">{{ loginError }}</p>
        </div>
      </div>
    </div>

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
      <div v-if="!showForm" class="vehicle-list">
        <div class="list-header">
          <span>Total: {{ vehicles.length }} vehicles</span>
          <button class="btn-refresh" @click="loadVehicles" :disabled="listLoading">
            {{ listLoading ? 'Loading...' : 'Refresh' }}
          </button>
        </div>
        <table class="vehicle-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Image</th>
              <th>Name</th>
              <th>Type</th>
              <th>Range</th>
              <th>Status</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="v in vehicles" :key="v.id">
              <td>{{ v.id }}</td>
              <td><img :src="v.coverImage" :alt="v.name" class="thumb" /></td>
              <td>{{ v.name }}</td>
              <td>{{ v.type }}</td>
              <td>{{ v.range }} km</td>
              <td>
                <label class="switch">
                  <input type="checkbox" :checked="v.enabled" @change="toggleEnabled(v)" />
                  <span class="slider"></span>
                </label>
              </td>
              <td class="actions-cell">
                <button class="btn-edit" @click="openEditForm(v)">Edit</button>
                <button class="btn-delete" @click="confirmDelete(v)">Delete</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- 新增/编辑表单 -->
      <div v-if="showForm" class="form-container">
        <h2>{{ isEditing ? 'Edit Vehicle' : 'Add New Vehicle' }}</h2>

        <!-- 品牌数据库快速填充 -->
        <div v-if="brandsData.length > 0" class="db-selector-card">
          <h3 class="db-selector-title">Quick Fill from Database</h3>
          <p class="db-selector-hint">Select brand, model and variant to auto-fill the form fields below.</p>
          <div class="db-selector-row">
            <div class="db-selector-group">
              <label>Brand</label>
              <select v-model="selectedBrand" @change="onBrandChange">
                <option value="">-- Select Brand --</option>
                <option v-for="b in brandsData" :key="b.nameEn" :value="b.nameEn">
                  {{ b.nameEn }}
                </option>
              </select>
            </div>
            <div class="db-selector-group">
              <label>Model</label>
              <select v-model="selectedModel" @change="onModelChange" :disabled="!selectedBrand">
                <option value="">-- Select Model --</option>
                <option v-for="m in currentModels()" :key="m.nameEn" :value="m.nameEn">
                  {{ m.nameEn }}
                </option>
              </select>
            </div>
            <div class="db-selector-group">
              <label>Variant</label>
              <select v-model="selectedVariant" :disabled="!selectedModel">
                <option value="">-- Select Variant --</option>
                <option v-for="v in currentVariants()" :key="v.specNameEn" :value="v.specNameEn">
                  {{ v.specNameEn }} ({{ v.range }}km)
                </option>
              </select>
            </div>
            <button class="btn-apply-variant" @click="applyVariant" :disabled="!selectedVariant">
              Apply
            </button>
          </div>
        </div>
        <div v-else-if="brandsLoading" class="db-selector-card">
          <p style="text-align:center; color:#999;">Loading brands database...</p>
        </div>

        <div class="form-grid">
          <div class="form-group">
            <label>Name *</label>
            <input v-model="form.name" type="text" placeholder="e.g. 2025 BYD Song Plus" />
          </div>
          <div class="form-group">
            <label>Slug *</label>
            <input v-model="form.slug" type="text" placeholder="e.g. song-plus" />
          </div>
          <div class="form-group">
            <label>Type *</label>
            <select v-model="form.type">
              <option value="SUV">SUV</option>
              <option value="SEDAN">SEDAN</option>
              <option value="VAN">VAN</option>
              <option value="PICKUP">PICKUP</option>
              <option value="TRUCK">TRUCK</option>
              <option value="REFRIGERATED">REFRIGERATED</option>
              <option value="BUS">BUS</option>
            </select>
          </div>
          <div class="form-group">
            <label>Range (km) *</label>
            <input v-model.number="form.range" type="number" placeholder="e.g. 520" />
          </div>
          <div class="form-group">
            <label>Seats *</label>
            <input v-model.number="form.seats" type="number" placeholder="e.g. 5" />
          </div>
          <div class="form-group">
            <label>Configuration</label>
            <select v-model="form.configuration">
              <option value="Basic">Basic</option>
              <option value="Premium">Premium</option>
              <option value="Commercial">Commercial</option>
            </select>
          </div>
          <div class="form-group full-width">
            <label>Description</label>
            <textarea v-model="form.description" rows="4" placeholder="Vehicle description..."></textarea>
          </div>
        </div>

        <h3>Specifications</h3>
        <div class="form-grid">
          <div class="form-group">
            <label>Year</label>
            <input v-model="form.specs.year" type="text" placeholder="2025" />
          </div>
          <div class="form-group">
            <label>Make</label>
            <input v-model="form.specs.make" type="text" placeholder="BYD" />
          </div>
          <div class="form-group">
            <label>Model</label>
            <input v-model="form.specs.model" type="text" placeholder="Song Plus" />
          </div>
          <div class="form-group">
            <label>Category</label>
            <input v-model="form.specs.category" type="text" placeholder="PASSENGER" />
          </div>
          <div class="form-group">
            <label>Battery Capacity</label>
            <input v-model="form.specs.batteryCapacity" type="text" placeholder="71.7 kWh" />
          </div>
        </div>

        <h3>Colors</h3>
        <div class="colors-editor">
          <div v-for="(color, idx) in form.colors" :key="idx" class="color-item">
            <span class="color-swatch" :style="{ background: color }"></span>
            <span>{{ getColorName(color) }}</span>
            <button class="btn-remove-sm" @click="form.colors.splice(idx, 1)">x</button>
          </div>
          <div class="color-add-row">
            <select v-model="selectedColorToAdd">
              <option value="">-- Select Color --</option>
              <option v-for="c in availableColors()" :key="c.hex" :value="c.hex">
                {{ c.name }}
              </option>
            </select>
            <button class="btn-add-color" @click="addSelectedColor" :disabled="!selectedColorToAdd">+ Add</button>
          </div>
        </div>

        <h3>Cover Image</h3>
        <div class="image-upload-section">
          <div v-if="form.coverImage" class="current-cover">
            <img :src="form.coverImage" alt="Cover" class="preview-img" />
          </div>
          <input type="file" accept="image/*" @change="handleCoverUpload" ref="coverInput" />
        </div>

        <h3>Detail Images</h3>
        <div class="image-upload-section">
          <div class="detail-images-grid">
            <div v-for="(img, idx) in form.detailImages" :key="idx" class="detail-img-item">
              <img :src="img" alt="Detail" class="preview-img-sm" />
              <button class="btn-remove-sm" @click="removeDetailImage(idx)">x</button>
            </div>
          </div>
          <input type="file" accept="image/*" multiple @change="handleDetailUpload" ref="detailInput" />
        </div>

        <div class="form-actions">
          <button class="btn-save" @click="saveVehicle" :disabled="saving">
            {{ saving ? 'Saving...' : 'Save' }}
          </button>
          <button class="btn-cancel" @click="cancelForm">Cancel</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue'
import { validateToken, getFileContent, updateFile, uploadImage, deployToMain } from '@/utils/github.js'

// 认证状态
const authenticated = ref(false)
const tokenInput = ref('')
const loginLoading = ref(false)
const loginError = ref('')
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
const coverInput = ref(null)
const detailInput = ref(null)

// 状态提示
const statusMsg = ref('')
const statusType = ref('info')

// 待上传的新文件
const pendingCoverFile = ref(null)
const pendingDetailFiles = ref([])

// 预定义汽车颜色
const CAR_COLORS = [
  { name: 'White', hex: '#FFFFFF' },
  { name: 'Black', hex: '#000000' },
  { name: 'Silver', hex: '#C0C0C0' },
  { name: 'Gray', hex: '#808080' },
  { name: 'Light Gray', hex: '#D3D3D3' },
  { name: 'Red', hex: '#FF0000' },
  { name: 'Dark Red', hex: '#8B0000' },
  { name: 'Blue', hex: '#0000FF' },
  { name: 'Dark Blue', hex: '#00008B' },
  { name: 'Navy Blue', hex: '#0011FF' },
  { name: 'Green', hex: '#008000' },
  { name: 'Dark Green', hex: '#006400' },
  { name: 'Yellow', hex: '#FFD700' },
  { name: 'Orange', hex: '#FF8C00' },
  { name: 'Brown', hex: '#8B4513' },
  { name: 'Beige', hex: '#F5F5DC' },
  { name: 'Champagne', hex: '#F7E7CE' },
  { name: 'Pearl', hex: '#FDEEF4' },
  { name: 'Coral', hex: '#FF6B6B' },
  { name: 'Teal', hex: '#4ECDC4' },
  { name: 'Lemon', hex: '#FFE66D' }
]

// 根据十六进制色值返回颜色名称
function getColorName(hex) {
  const found = CAR_COLORS.find(c => c.hex.toUpperCase() === hex.toUpperCase())
  return found ? found.name : hex
}

// 返回尚未被选中的可用颜色
function availableColors() {
  const selected = form.colors.map(c => c.toUpperCase())
  return CAR_COLORS.filter(c => !selected.includes(c.hex.toUpperCase()))
}

// 添加选中的颜色到表单
function addSelectedColor() {
  if (!selectedColorToAdd.value) return
  form.colors.push(selectedColorToAdd.value)
  selectedColorToAdd.value = ''
}

const selectedColorToAdd = ref('')

// 品牌数据库（级联选择器）
const brandsData = ref([])
const brandsLoading = ref(false)
const selectedBrand = ref('')
const selectedModel = ref('')
const selectedVariant = ref('')

// 计算当前选中品牌下的车系列表
function currentModels() {
  const brand = brandsData.value.find(b => b.nameEn === selectedBrand.value)
  return brand ? brand.models : []
}

// 计算当前选中车系下的配置列表
function currentVariants() {
  const models = currentModels()
  const model = models.find(m => m.nameEn === selectedModel.value)
  return model ? model.variants : []
}

// 品牌选择变化时重置下级
function onBrandChange() {
  selectedModel.value = ''
  selectedVariant.value = ''
}

// 车系选择变化时重置配置
function onModelChange() {
  selectedVariant.value = ''
}

// 选择配置后自动填充表单
function applyVariant() {
  if (!selectedVariant.value) return
  const brand = brandsData.value.find(b => b.nameEn === selectedBrand.value)
  if (!brand) return
  const model = brand.models.find(m => m.nameEn === selectedModel.value)
  if (!model) return
  const variant = model.variants.find(v => v.specNameEn === selectedVariant.value)
  if (!variant) return

  form.name = `${variant.year} ${brand.nameEn} ${model.nameEn}`
  form.slug = autoSlug(form.name)
  form.type = variant.type || 'SUV'
  form.range = variant.range || 0
  form.seats = variant.seats || 5
  form.specs.year = variant.year || '2025'
  form.specs.make = brand.nameEn
  form.specs.model = model.nameEn
  form.specs.batteryCapacity = variant.batteryCapacity || 'N/A'
  form.specs.category = 'PASSENGER'

  showStatus('Auto-filled from database: ' + form.name, 'success')
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
      console.log(`Loaded ${brandsData.value.length} brands from database`)
    }
  } catch (err) {
    console.warn('Failed to load brands database:', err)
  } finally {
    brandsLoading.value = false
  }
}

const emptyForm = () => ({
  name: '',
  slug: '',
  type: 'SUV',
  range: 0,
  seats: 5,
  configuration: 'Basic',
  description: '',
  coverImage: '',
  colors: ['#000000'],
  specs: {
    year: '2025',
    make: '',
    model: '',
    category: '',
    batteryCapacity: 'N/A'
  },
  detailImages: []
})

const form = reactive(emptyForm())

// 自动从名称生成 slug
function autoSlug(name) {
  return name.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '')
}

// 登录
async function handleLogin() {
  loginLoading.value = true
  loginError.value = ''
  try {
    const result = await validateToken(tokenInput.value)
    if (result.valid) {
      token = tokenInput.value
      authenticated.value = true
      sessionStorage.setItem('gh_token', token)
      await loadVehicles()
      loadBrandsData()
    } else {
      loginError.value = result.message
    }
  } catch (err) {
    loginError.value = err.message
  } finally {
    loginLoading.value = false
  }
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

// 切换启用/禁用
async function toggleEnabled(vehicle) {
  vehicle.enabled = !vehicle.enabled
  await saveAllVehicles('Toggle vehicle: ' + vehicle.name)
}

// 打开新增表单
function openAddForm() {
  Object.assign(form, emptyForm())
  pendingCoverFile.value = null
  pendingDetailFiles.value = []
  isEditing.value = false
  editingId.value = null
  showForm.value = true
}

// 打开编辑表单
function openEditForm(vehicle) {
  Object.assign(form, {
    name: vehicle.name,
    slug: vehicle.slug,
    type: vehicle.type,
    range: vehicle.range,
    seats: vehicle.seats,
    configuration: vehicle.configuration,
    description: vehicle.description,
    coverImage: vehicle.coverImage,
    colors: [...vehicle.colors],
    specs: { ...vehicle.specs },
    detailImages: [...vehicle.detailImages]
  })
  pendingCoverFile.value = null
  pendingDetailFiles.value = []
  isEditing.value = true
  editingId.value = vehicle.id
  showForm.value = true
}

function cancelForm() {
  showForm.value = false
}

// 处理封面图上传
function handleCoverUpload(e) {
  const file = e.target.files[0]
  if (!file) return
  pendingCoverFile.value = file
  // 本地预览
  const reader = new FileReader()
  reader.onload = (ev) => {
    form.coverImage = ev.target.result
  }
  reader.readAsDataURL(file)
}

// 处理详情图上传
function handleDetailUpload(e) {
  const files = Array.from(e.target.files)
  files.forEach(file => {
    pendingDetailFiles.value.push(file)
    const reader = new FileReader()
    reader.onload = (ev) => {
      form.detailImages.push(ev.target.result)
    }
    reader.readAsDataURL(file)
  })
}

// 移除详情图
function removeDetailImage(idx) {
  form.detailImages.splice(idx, 1)
  // 同步移除待上传文件
  if (idx < pendingDetailFiles.value.length) {
    pendingDetailFiles.value.splice(idx, 1)
  }
}

// 将文件转 Base64（不含前缀）
function fileToBase64(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader()
    reader.onload = () => {
      const base64 = reader.result.split(',')[1]
      resolve(base64)
    }
    reader.onerror = reject
    reader.readAsDataURL(file)
  })
}

// 显示状态消息
function showStatus(msg, type = 'info') {
  statusMsg.value = msg
  statusType.value = type
  setTimeout(() => { statusMsg.value = '' }, 5000)
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
    // SHA 不匹配时自动重试：重新获取最新 SHA 再保存一次
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

// 一键部署到前台网站（将 source 分支数据同步到 main 分支）
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

// 保存车辆（新增或编辑）
async function saveVehicle() {
  if (!form.name || !form.slug || !form.type) {
    showStatus('Please fill in all required fields.', 'error')
    return
  }
  saving.value = true
  try {
    const slug = form.slug
    // 上传封面图
    if (pendingCoverFile.value) {
      const ext = pendingCoverFile.value.name.split('.').pop()
      const coverPath = `public/vehicles/${slug}/cover.${ext}`
      const b64 = await fileToBase64(pendingCoverFile.value)
      await uploadImage(token, coverPath, b64, `Upload cover for ${form.name}`)
      form.coverImage = `/vehicles/${slug}/cover.${ext}`
    }

    // 上传详情图
    const existingCount = form.detailImages.length - pendingDetailFiles.value.length
    for (let i = 0; i < pendingDetailFiles.value.length; i++) {
      const file = pendingDetailFiles.value[i]
      const ext = file.name.split('.').pop()
      const imgPath = `public/vehicles/${slug}/${existingCount + i + 1}.${ext}`
      const b64 = await fileToBase64(file)
      await uploadImage(token, imgPath, b64, `Upload image for ${form.name}`)
      // 替换预览 URL 为实际路径
      form.detailImages[existingCount + i] = `/vehicles/${slug}/${existingCount + i + 1}.${ext}`
    }

    // 构建车辆对象
    const vehicleData = {
      id: isEditing.value ? editingId.value : (Math.max(0, ...vehicles.value.map(v => v.id)) + 1),
      slug: form.slug,
      enabled: true,
      name: form.name,
      type: form.type,
      range: form.range,
      seats: form.seats,
      configuration: form.configuration,
      coverImage: form.coverImage,
      colors: [...form.colors],
      description: form.description,
      specs: { ...form.specs },
      detailImages: [...form.detailImages]
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

    await saveAllVehicles(isEditing.value ? `Update vehicle: ${form.name}` : `Add vehicle: ${form.name}`)
    showForm.value = false
    pendingCoverFile.value = null
    pendingDetailFiles.value = []
  } catch (err) {
    showStatus('Save failed: ' + err.message, 'error')
  } finally {
    saving.value = false
  }
}

onMounted(() => {
  // 尝试从 sessionStorage 恢复登录
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

/* 登录界面 */
.login-container {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: linear-gradient(135deg, var(--primary-color), var(--dark-color));
}

.login-card {
  background: #fff;
  padding: 2.5rem;
  border-radius: 1rem;
  box-shadow: var(--shadow-lg);
  width: 420px;
  max-width: 90vw;
  text-align: center;
}

.login-card h1 {
  color: var(--primary-color);
  margin-bottom: 0.5rem;
  font-size: 1.75rem;
  font-weight: 700;
}

.login-desc {
  color: #64748b;
  margin-bottom: 1.5rem;
  font-size: 0.875rem;
  line-height: 1.5;
}

.login-form input {
  width: 100%;
  padding: 0.75rem 1rem;
  border: 2px solid #e2e8f0;
  border-radius: 0.75rem;
  font-size: 0.875rem;
  box-sizing: border-box;
  margin-bottom: 1rem;
  transition: border-color 0.2s, box-shadow 0.2s;
  font-family: inherit;
}

.login-form input:focus {
  outline: none;
  border-color: var(--accent-color);
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}

.login-form button {
  width: 100%;
  padding: 0.75rem;
  background: var(--accent-color);
  color: #fff;
  border: none;
  border-radius: 9999px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  font-family: inherit;
  min-height: 44px;
}

.login-form button:hover {
  background: var(--accent-color-dark);
  transform: translateY(-1px);
  box-shadow: var(--shadow);
}

.login-form button:disabled {
  background: #94a3b8;
  cursor: not-allowed;
  transform: none;
  box-shadow: none;
}

.error-msg {
  color: #ef4444;
  margin-top: 0.75rem;
  font-size: 0.875rem;
  font-weight: 500;
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
  background: #10b981;
  color: #fff;
  border: none;
  padding: 0.625rem 1.25rem;
  border-radius: 9999px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  font-family: inherit;
  min-height: 44px;
  font-size: 0.875rem;
}

.btn-add:hover {
  background: #059669;
  transform: translateY(-1px);
}

.btn-deploy {
  background: var(--accent-color);
  color: #fff;
  border: none;
  padding: 0.625rem 1.25rem;
  border-radius: 9999px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  font-family: inherit;
  min-height: 44px;
  font-size: 0.875rem;
}

.btn-deploy:hover {
  background: var(--accent-color-dark);
  transform: translateY(-1px);
}

.btn-deploy:disabled {
  background: #94a3b8;
  cursor: not-allowed;
  transform: none;
}

.btn-logout {
  background: transparent;
  color: #fff;
  border: 1px solid rgba(255, 255, 255, 0.3);
  padding: 0.625rem 1.25rem;
  border-radius: 9999px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  font-family: inherit;
  min-height: 44px;
  font-size: 0.875rem;
}

.btn-logout:hover {
  background: rgba(255, 255, 255, 0.1);
  border-color: rgba(255, 255, 255, 0.5);
}

/* 状态条 */
.status-bar {
  padding: 0.875rem 1.25rem;
  border-radius: 0.75rem;
  margin-bottom: 1.5rem;
  font-weight: 600;
  font-size: 0.875rem;
  border-left: 4px solid transparent;
}

.status-bar.success {
  background: #ecfdf5;
  color: #065f46;
  border-left-color: #10b981;
}

.status-bar.error {
  background: #fef2f2;
  color: #991b1b;
  border-left-color: #ef4444;
}

.status-bar.info {
  background: #eff6ff;
  color: #1e40af;
  border-left-color: var(--accent-color);
}

/* 车辆列表 */
.list-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
  color: #64748b;
  font-weight: 500;
}

.btn-refresh {
  background: var(--accent-color);
  color: #fff;
  border: none;
  padding: 0.5rem 1.25rem;
  border-radius: 9999px;
  cursor: pointer;
  font-weight: 600;
  font-size: 0.875rem;
  transition: all 0.2s;
  font-family: inherit;
  min-height: 40px;
}

.btn-refresh:hover {
  background: var(--accent-color-dark);
  transform: translateY(-1px);
}

.btn-refresh:disabled {
  background: #94a3b8;
  cursor: not-allowed;
  transform: none;
}

.vehicle-list {
  overflow-x: auto;
}

.vehicle-table {
  width: 100%;
  border-collapse: collapse;
  background: #fff;
  border-radius: 0.75rem;
  overflow: hidden;
  box-shadow: var(--shadow);
  min-width: 700px;
}

.vehicle-table th {
  background: var(--primary-color);
  color: #fff;
  padding: 0.875rem 1rem;
  text-align: left;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.vehicle-table td {
  padding: 0.75rem 1rem;
  border-bottom: 1px solid #f1f5f9;
  font-size: 0.875rem;
  vertical-align: middle;
}

.vehicle-table tbody tr:hover {
  background: #f8fafc;
}

.thumb {
  width: 64px;
  height: 42px;
  object-fit: cover;
  border-radius: 0.5rem;
}

.actions-cell {
  display: flex;
  gap: 0.5rem;
  align-items: center;
}

.btn-edit {
  background: var(--accent-color);
  color: #fff;
  border: none;
  padding: 0.375rem 1rem;
  border-radius: 9999px;
  cursor: pointer;
  font-size: 0.8rem;
  font-weight: 600;
  transition: all 0.2s;
  font-family: inherit;
  min-height: 36px;
}

.btn-edit:hover {
  background: var(--accent-color-dark);
}

.btn-delete {
  background: #ef4444;
  color: #fff;
  border: none;
  padding: 0.375rem 1rem;
  border-radius: 9999px;
  cursor: pointer;
  font-size: 0.8rem;
  font-weight: 600;
  transition: all 0.2s;
  font-family: inherit;
  min-height: 36px;
}

.btn-delete:hover {
  background: #dc2626;
}

/* Toggle Switch */
.switch {
  position: relative;
  display: inline-block;
  width: 44px;
  height: 24px;
}

.switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

.slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #cbd5e1;
  transition: 0.3s;
  border-radius: 24px;
}

.slider:before {
  position: absolute;
  content: "";
  height: 18px;
  width: 18px;
  left: 3px;
  bottom: 3px;
  background-color: white;
  transition: 0.3s;
  border-radius: 50%;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.15);
}

input:checked + .slider {
  background-color: #10b981;
}

input:checked + .slider:before {
  transform: translateX(20px);
}

/* 表单 */
.form-container {
  background: #fff;
  padding: 2rem;
  border-radius: 0.75rem;
  box-shadow: var(--shadow);
}

.form-container h2 {
  color: var(--primary-color);
  margin-bottom: 1.5rem;
  font-size: 1.5rem;
  font-weight: 700;
}

.form-container h3 {
  color: var(--primary-color);
  margin: 1.75rem 0 1rem;
  border-bottom: 2px solid #f1f5f9;
  padding-bottom: 0.5rem;
  font-size: 1.1rem;
  font-weight: 600;
}

/* 品牌数据库选择器 */
.db-selector-card {
  background: #f0f9ff;
  border: none;
  border-left: 4px solid var(--accent-color);
  border-radius: 0.75rem;
  padding: 1.25rem;
  margin-bottom: 1.5rem;
}

.db-selector-title {
  color: var(--accent-color) !important;
  margin: 0 0 0.25rem 0 !important;
  border-bottom: none !important;
  padding-bottom: 0 !important;
  font-size: 1rem;
}

.db-selector-hint {
  color: #64748b;
  font-size: 0.8rem;
  margin: 0 0 1rem 0;
}

.db-selector-row {
  display: flex;
  gap: 0.75rem;
  align-items: flex-end;
  flex-wrap: wrap;
}

.db-selector-group {
  display: flex;
  flex-direction: column;
  flex: 1;
  min-width: 160px;
}

.db-selector-group label {
  font-weight: 600;
  color: var(--primary-color);
  margin-bottom: 0.375rem;
  font-size: 0.8rem;
}

.db-selector-group select {
  padding: 0.5rem 0.75rem;
  border: 2px solid #e2e8f0;
  border-radius: 0.5rem;
  font-size: 0.875rem;
  background: #fff;
  transition: border-color 0.2s, box-shadow 0.2s;
  font-family: inherit;
  min-height: 42px;
}

.db-selector-group select:focus {
  outline: none;
  border-color: var(--accent-color);
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}

.db-selector-group select:disabled {
  background: #f8fafc;
  color: #94a3b8;
  cursor: not-allowed;
}

.btn-apply-variant {
  padding: 0.5rem 1.5rem;
  background: var(--accent-color);
  color: #fff;
  border: none;
  border-radius: 9999px;
  font-size: 0.875rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  white-space: nowrap;
  align-self: flex-end;
  font-family: inherit;
  min-height: 42px;
}

.btn-apply-variant:hover:not(:disabled) {
  background: var(--accent-color-dark);
  transform: translateY(-1px);
}

.btn-apply-variant:disabled {
  background: #cbd5e1;
  cursor: not-allowed;
}

.form-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.form-group {
  display: flex;
  flex-direction: column;
}

.form-group.full-width {
  grid-column: 1 / -1;
}

.form-group label {
  font-weight: 600;
  color: var(--primary-color);
  margin-bottom: 0.375rem;
  font-size: 0.8rem;
}

.form-group input,
.form-group select,
.form-group textarea {
  padding: 0.625rem 0.75rem;
  border: 2px solid #e2e8f0;
  border-radius: 0.5rem;
  font-size: 0.875rem;
  transition: border-color 0.2s, box-shadow 0.2s;
  font-family: inherit;
  min-height: 42px;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
  outline: none;
  border-color: var(--accent-color);
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}

/* 颜色编辑器 */
.colors-editor {
  display: flex;
  flex-wrap: wrap;
  gap: 0.625rem;
  align-items: center;
}

.color-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: #f1f5f9;
  padding: 0.375rem 0.75rem;
  border-radius: 9999px;
  font-size: 0.8rem;
  font-weight: 500;
}

.color-swatch {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  border: 2px solid #e2e8f0;
  display: inline-block;
  flex-shrink: 0;
}

.color-add-row {
  display: flex;
  gap: 0.5rem;
  align-items: center;
  width: 100%;
  margin-top: 0.5rem;
}

.color-add-row select {
  flex: 1;
  padding: 0.5rem 0.75rem;
  border: 2px solid #e2e8f0;
  border-radius: 0.5rem;
  font-size: 0.875rem;
  background: #fff;
  transition: border-color 0.2s, box-shadow 0.2s;
  font-family: inherit;
  min-height: 42px;
}

.color-add-row select:focus {
  outline: none;
  border-color: var(--accent-color);
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}

.btn-remove-sm {
  background: #ef4444;
  color: #fff;
  border: none;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  cursor: pointer;
  font-size: 0.75rem;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.2s;
  flex-shrink: 0;
}

.btn-remove-sm:hover {
  background: #dc2626;
}

.btn-add-color {
  background: #10b981;
  color: #fff;
  border: none;
  padding: 0.5rem 1.25rem;
  border-radius: 9999px;
  cursor: pointer;
  font-weight: 600;
  font-size: 0.875rem;
  white-space: nowrap;
  transition: all 0.2s;
  font-family: inherit;
  min-height: 42px;
}

.btn-add-color:hover:not(:disabled) {
  background: #059669;
  transform: translateY(-1px);
}

.btn-add-color:disabled {
  background: #cbd5e1;
  cursor: not-allowed;
}

/* 图片上传 */
.image-upload-section {
  margin-bottom: 0.75rem;
}

.image-upload-section input[type="file"] {
  font-size: 0.875rem;
  color: #64748b;
  font-family: inherit;
}

.image-upload-section input[type="file"]::file-selector-button {
  background: var(--accent-color);
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 9999px;
  font-weight: 600;
  font-size: 0.8rem;
  cursor: pointer;
  margin-right: 0.75rem;
  transition: all 0.2s;
  font-family: inherit;
}

.image-upload-section input[type="file"]::file-selector-button:hover {
  background: var(--accent-color-dark);
}

.current-cover {
  margin-bottom: 0.75rem;
}

.preview-img {
  max-width: 200px;
  max-height: 120px;
  object-fit: cover;
  border-radius: 0.75rem;
  border: 2px solid #f1f5f9;
}

.detail-images-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  margin-bottom: 0.75rem;
}

.detail-img-item {
  position: relative;
}

.preview-img-sm {
  width: 100px;
  height: 75px;
  object-fit: cover;
  border-radius: 0.5rem;
  border: 2px solid #f1f5f9;
}

.detail-img-item .btn-remove-sm {
  position: absolute;
  top: -8px;
  right: -8px;
}

/* 表单操作按钮 */
.form-actions {
  display: flex;
  gap: 0.75rem;
  margin-top: 2rem;
  padding-top: 1.5rem;
  border-top: 2px solid #f1f5f9;
}

.btn-save {
  background: #10b981;
  color: #fff;
  border: none;
  padding: 0.75rem 2rem;
  border-radius: 9999px;
  font-weight: 600;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.2s;
  font-family: inherit;
  min-height: 48px;
}

.btn-save:hover {
  background: #059669;
  transform: translateY(-1px);
  box-shadow: var(--shadow);
}

.btn-save:disabled {
  background: #94a3b8;
  cursor: not-allowed;
  transform: none;
  box-shadow: none;
}

.btn-cancel {
  background: #64748b;
  color: #fff;
  border: none;
  padding: 0.75rem 2rem;
  border-radius: 9999px;
  font-weight: 600;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.2s;
  font-family: inherit;
  min-height: 48px;
}

.btn-cancel:hover {
  background: #475569;
  transform: translateY(-1px);
}

/* ==================== 响应式：768px ==================== */
@media (max-width: 768px) {
  .admin-container {
    padding: 1rem;
  }

  .admin-header {
    flex-direction: column;
    gap: 1rem;
    text-align: center;
    padding: 1rem;
  }

  .admin-header h1 {
    font-size: 1.25rem;
  }

  .header-actions {
    flex-wrap: wrap;
    justify-content: center;
    width: 100%;
  }

  .header-actions button {
    flex: 1;
    min-width: 120px;
  }

  /* 表格转卡片布局 */
  .vehicle-table {
    min-width: unset;
  }

  .vehicle-table thead {
    display: none;
  }

  .vehicle-table tbody {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
  }

  .vehicle-table tr {
    display: flex;
    flex-wrap: wrap;
    background: #fff;
    border-radius: 0.75rem;
    box-shadow: var(--shadow-sm);
    padding: 1rem;
    border: 1px solid #f1f5f9;
    gap: 0.5rem;
  }

  .vehicle-table td {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0.375rem 0;
    border-bottom: none;
    font-size: 0.875rem;
    width: 100%;
  }

  .vehicle-table td::before {
    font-weight: 600;
    color: #64748b;
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    min-width: 70px;
  }

  .vehicle-table td:nth-child(1)::before { content: 'ID'; }
  .vehicle-table td:nth-child(2)::before { content: 'Image'; }
  .vehicle-table td:nth-child(3)::before { content: 'Name'; }
  .vehicle-table td:nth-child(4)::before { content: 'Type'; }
  .vehicle-table td:nth-child(5)::before { content: 'Range'; }
  .vehicle-table td:nth-child(6)::before { content: 'Status'; }
  .vehicle-table td:nth-child(7)::before { content: 'Actions'; }

  .thumb {
    width: 80px;
    height: 52px;
  }

  .actions-cell {
    justify-content: flex-end;
    gap: 0.5rem;
    padding-top: 0.5rem !important;
    border-top: 1px solid #f1f5f9 !important;
  }

  .btn-edit,
  .btn-delete {
    min-height: 44px;
    padding: 0.5rem 1.25rem;
    font-size: 0.875rem;
  }

  /* 表单 */
  .form-container {
    padding: 1.25rem;
  }

  .form-grid {
    grid-template-columns: 1fr;
  }

  .db-selector-row {
    flex-direction: column;
  }

  .db-selector-group {
    min-width: 100%;
  }

  .form-actions {
    flex-direction: column;
  }

  .form-actions button {
    width: 100%;
  }
}

/* ==================== 响应式：480px ==================== */
@media (max-width: 480px) {
  .admin-container {
    padding: 0.75rem;
  }

  .admin-header {
    border-radius: 0.5rem;
    padding: 0.875rem;
  }

  .admin-header h1 {
    font-size: 1.1rem;
  }

  .header-actions button {
    font-size: 0.8rem;
    padding: 0.5rem 1rem;
  }

  .login-card {
    padding: 1.5rem;
  }

  .login-card h1 {
    font-size: 1.35rem;
  }

  .form-container {
    padding: 1rem;
  }

  .form-container h2 {
    font-size: 1.25rem;
  }

  .db-selector-card {
    padding: 1rem;
  }

  .detail-images-grid {
    gap: 0.5rem;
  }

  .preview-img-sm {
    width: 72px;
    height: 54px;
  }
}
</style>