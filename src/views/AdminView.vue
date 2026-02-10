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
            <input type="color" v-model="form.colors[idx]" />
            <span>{{ color }}</span>
            <button class="btn-remove-sm" @click="form.colors.splice(idx, 1)">x</button>
          </div>
          <button class="btn-add-color" @click="form.colors.push('#000000')">+ Add Color</button>
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
import { validateToken, getFileContent, updateFile, uploadImage } from '@/utils/github.js'

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
const coverInput = ref(null)
const detailInput = ref(null)

// 状态提示
const statusMsg = ref('')
const statusType = ref('info')

// 待上传的新文件
const pendingCoverFile = ref(null)
const pendingDetailFiles = ref([])

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

// 保存所有车辆数据到 GitHub
async function saveAllVehicles(commitMsg) {
  try {
    const content = JSON.stringify(vehicles.value, null, 2)
    const result = await updateFile(token, 'public/data/vehicles.json', content, vehiclesFileSha.value, commitMsg)
    vehiclesFileSha.value = result.content.sha
    showStatus('Saved successfully! Site will update in 1-2 minutes.', 'success')
  } catch (err) {
    showStatus('Save failed: ' + err.message, 'error')
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
  }
})
</script>


<style scoped>
.admin-page {
  min-height: 100vh;
  background: #f0f2f5;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

/* 登录界面 */
.login-container {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: linear-gradient(135deg, #001f3f 0%, #003366 100%);
}

.login-card {
  background: #fff;
  padding: 40px;
  border-radius: 12px;
  box-shadow: 0 10px 40px rgba(0,0,0,0.2);
  width: 400px;
  max-width: 90vw;
  text-align: center;
}

.login-card h1 {
  color: #001f3f;
  margin-bottom: 10px;
}

.login-desc {
  color: #666;
  margin-bottom: 20px;
  font-size: 14px;
}

.login-form input {
  width: 100%;
  padding: 12px;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  font-size: 14px;
  box-sizing: border-box;
  margin-bottom: 12px;
  transition: border-color 0.3s;
}

.login-form input:focus {
  outline: none;
  border-color: #0074D9;
}

.login-form button {
  width: 100%;
  padding: 12px;
  background: #0074D9;
  color: #fff;
  border: none;
  border-radius: 8px;
  font-size: 16px;
  font-weight: bold;
  cursor: pointer;
  transition: background 0.3s;
}

.login-form button:hover { background: #005fa3; }
.login-form button:disabled { background: #999; cursor: not-allowed; }

.error-msg {
  color: #e74c3c;
  margin-top: 10px;
  font-size: 14px;
}

/* 管理界面 */
.admin-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.admin-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 0;
  border-bottom: 2px solid #e0e0e0;
  margin-bottom: 20px;
}

.admin-header h1 {
  color: #001f3f;
  margin: 0;
}

.header-actions {
  display: flex;
  gap: 10px;
}

.btn-add {
  background: #27ae60;
  color: #fff;
  border: none;
  padding: 10px 20px;
  border-radius: 8px;
  font-weight: bold;
  cursor: pointer;
  transition: background 0.3s;
}

.btn-add:hover { background: #219a52; }

.btn-logout {
  background: #e74c3c;
  color: #fff;
  border: none;
  padding: 10px 20px;
  border-radius: 8px;
  font-weight: bold;
  cursor: pointer;
  transition: background 0.3s;
}

.btn-logout:hover { background: #c0392b; }

/* 状态条 */
.status-bar {
  padding: 12px 20px;
  border-radius: 8px;
  margin-bottom: 20px;
  font-weight: bold;
}

.status-bar.success { background: #d4edda; color: #155724; }
.status-bar.error { background: #f8d7da; color: #721c24; }
.status-bar.info { background: #d1ecf1; color: #0c5460; }

/* 车辆列表 */
.list-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 15px;
  color: #666;
}

.btn-refresh {
  background: #0074D9;
  color: #fff;
  border: none;
  padding: 8px 16px;
  border-radius: 6px;
  cursor: pointer;
}

.btn-refresh:disabled { background: #999; }

.vehicle-table {
  width: 100%;
  border-collapse: collapse;
  background: #fff;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 10px rgba(0,0,0,0.08);
}

.vehicle-table th {
  background: #001f3f;
  color: #fff;
  padding: 12px;
  text-align: left;
  font-size: 14px;
}

.vehicle-table td {
  padding: 10px 12px;
  border-bottom: 1px solid #eee;
  font-size: 14px;
  vertical-align: middle;
}

.thumb {
  width: 60px;
  height: 40px;
  object-fit: cover;
  border-radius: 4px;
}

.actions-cell {
  display: flex;
  gap: 6px;
}

.btn-edit {
  background: #0074D9;
  color: #fff;
  border: none;
  padding: 6px 12px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 12px;
}

.btn-delete {
  background: #e74c3c;
  color: #fff;
  border: none;
  padding: 6px 12px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 12px;
}

/* Toggle Switch */
.switch {
  position: relative;
  display: inline-block;
  width: 44px;
  height: 24px;
}

.switch input { opacity: 0; width: 0; height: 0; }

.slider {
  position: absolute;
  cursor: pointer;
  top: 0; left: 0; right: 0; bottom: 0;
  background-color: #ccc;
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
}

input:checked + .slider { background-color: #27ae60; }
input:checked + .slider:before { transform: translateX(20px); }

/* 表单 */
.form-container {
  background: #fff;
  padding: 30px;
  border-radius: 12px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.08);
}

.form-container h2 {
  color: #001f3f;
  margin-bottom: 20px;
}

.form-container h3 {
  color: #333;
  margin: 24px 0 12px;
  border-bottom: 1px solid #eee;
  padding-bottom: 8px;
}

.form-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
}

.form-group {
  display: flex;
  flex-direction: column;
}

.form-group.full-width {
  grid-column: 1 / -1;
}

.form-group label {
  font-weight: bold;
  color: #333;
  margin-bottom: 6px;
  font-size: 13px;
}

.form-group input,
.form-group select,
.form-group textarea {
  padding: 10px;
  border: 2px solid #e0e0e0;
  border-radius: 6px;
  font-size: 14px;
  transition: border-color 0.3s;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
  outline: none;
  border-color: #0074D9;
}

/* 颜色编辑器 */
.colors-editor {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  align-items: center;
}

.color-item {
  display: flex;
  align-items: center;
  gap: 6px;
  background: #f5f5f5;
  padding: 4px 8px;
  border-radius: 6px;
}

.color-item input[type="color"] {
  width: 30px;
  height: 30px;
  border: none;
  cursor: pointer;
}

.btn-remove-sm {
  background: #e74c3c;
  color: #fff;
  border: none;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  cursor: pointer;
  font-size: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.btn-add-color {
  background: #eee;
  border: 2px dashed #ccc;
  padding: 6px 14px;
  border-radius: 6px;
  cursor: pointer;
  color: #666;
}

/* 图片上传 */
.image-upload-section { margin-bottom: 10px; }

.preview-img {
  max-width: 200px;
  max-height: 120px;
  object-fit: cover;
  border-radius: 6px;
  margin-bottom: 8px;
}

.detail-images-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 10px;
}

.detail-img-item {
  position: relative;
}

.preview-img-sm {
  width: 80px;
  height: 60px;
  object-fit: cover;
  border-radius: 4px;
}

.detail-img-item .btn-remove-sm {
  position: absolute;
  top: -6px;
  right: -6px;
}

/* 表单操作按钮 */
.form-actions {
  display: flex;
  gap: 12px;
  margin-top: 24px;
  padding-top: 20px;
  border-top: 1px solid #eee;
}

.btn-save {
  background: #27ae60;
  color: #fff;
  border: none;
  padding: 12px 30px;
  border-radius: 8px;
  font-weight: bold;
  font-size: 16px;
  cursor: pointer;
}

.btn-save:disabled { background: #999; cursor: not-allowed; }

.btn-cancel {
  background: #95a5a6;
  color: #fff;
  border: none;
  padding: 12px 30px;
  border-radius: 8px;
  font-weight: bold;
  font-size: 16px;
  cursor: pointer;
}

@media (max-width: 768px) {
  .form-grid { grid-template-columns: 1fr; }
  .admin-header { flex-direction: column; gap: 10px; text-align: center; }
  .vehicle-table { font-size: 12px; }
  .thumb { width: 40px; height: 28px; }
}
</style>