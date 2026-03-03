<template>
  <div class="form-container">
    <h2>{{ isEditing ? 'Edit Vehicle' : 'Add New Vehicle' }}</h2>

    <!-- 品牌数据库快速填充 -->
    <BrandSelector
      :brandsData="brandsData"
      :brandsLoading="brandsLoading"
      @apply-variant="onApplyVariant"
    />

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
          <option v-for="c in availableColors" :key="c.hex" :value="c.hex">
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
      <button class="btn-save" @click="handleSave" :disabled="saving">
        {{ saving ? 'Saving...' : 'Save' }}
      </button>
      <button class="btn-cancel" @click="$emit('cancel')">Cancel</button>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, computed } from 'vue'
import BrandSelector from './BrandSelector.vue'

const props = defineProps({
  isEditing: { type: Boolean, default: false },
  initialData: { type: Object, default: null },
  brandsData: { type: Array, default: () => [] },
  brandsLoading: { type: Boolean, default: false },
  saving: { type: Boolean, default: false }
})

const emit = defineEmits(['save', 'cancel'])

const coverInput = ref(null)
const detailInput = ref(null)
const pendingCoverFile = ref(null)
const pendingDetailFiles = ref([])
const selectedColorToAdd = ref('')

// 预定义汽车颜色
const CAR_COLORS = [
  { name: 'White', hex: '#FFFFFF' }, { name: 'Black', hex: '#000000' },
  { name: 'Silver', hex: '#C0C0C0' }, { name: 'Gray', hex: '#808080' },
  { name: 'Light Gray', hex: '#D3D3D3' }, { name: 'Red', hex: '#FF0000' },
  { name: 'Dark Red', hex: '#8B0000' }, { name: 'Blue', hex: '#0000FF' },
  { name: 'Dark Blue', hex: '#00008B' }, { name: 'Navy Blue', hex: '#0011FF' },
  { name: 'Green', hex: '#008000' }, { name: 'Dark Green', hex: '#006400' },
  { name: 'Yellow', hex: '#FFD700' }, { name: 'Orange', hex: '#FF8C00' },
  { name: 'Brown', hex: '#8B4513' }, { name: 'Beige', hex: '#F5F5DC' },
  { name: 'Champagne', hex: '#F7E7CE' }, { name: 'Pearl', hex: '#FDEEF4' },
  { name: 'Coral', hex: '#FF6B6B' }, { name: 'Teal', hex: '#4ECDC4' },
  { name: 'Lemon', hex: '#FFE66D' }
]

const emptyForm = () => ({
  name: '', slug: '', type: 'SUV', range: 0, seats: 5,
  configuration: 'Basic', description: '', coverImage: '',
  colors: ['#000000'],
  specs: { year: '2025', make: '', model: '', category: '', batteryCapacity: 'N/A' },
  detailImages: []
})

const form = reactive(props.initialData ? { ...emptyForm(), ...props.initialData } : emptyForm())

pendingCoverFile.value = null
pendingDetailFiles.value = []

function autoSlug(name) {
  return name.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '')
}

function getColorName(hex) {
  const found = CAR_COLORS.find(c => c.hex.toUpperCase() === hex.toUpperCase())
  return found ? found.name : hex
}

const availableColors = computed(() => {
  const selected = form.colors.map(c => c.toUpperCase())
  return CAR_COLORS.filter(c => !selected.includes(c.hex.toUpperCase()))
})

function addSelectedColor() {
  if (!selectedColorToAdd.value) return
  form.colors.push(selectedColorToAdd.value)
  selectedColorToAdd.value = ''
}

function onApplyVariant(data) {
  form.name = data.name
  form.slug = autoSlug(data.name)
  form.type = data.type
  form.range = data.range
  form.seats = data.seats
  form.specs.year = data.year
  form.specs.make = data.make
  form.specs.model = data.model
  form.specs.batteryCapacity = data.batteryCapacity
  form.specs.category = 'PASSENGER'
}

function handleCoverUpload(e) {
  const file = e.target.files[0]
  if (!file) return
  pendingCoverFile.value = file
  const reader = new FileReader()
  reader.onload = (ev) => { form.coverImage = ev.target.result }
  reader.readAsDataURL(file)
}

function handleDetailUpload(e) {
  const files = Array.from(e.target.files)
  files.forEach(file => {
    pendingDetailFiles.value.push(file)
    const reader = new FileReader()
    reader.onload = (ev) => { form.detailImages.push(ev.target.result) }
    reader.readAsDataURL(file)
  })
}

function removeDetailImage(idx) {
  const existingCount = form.detailImages.length - pendingDetailFiles.value.length
  form.detailImages.splice(idx, 1)
  if (idx >= existingCount) {
    pendingDetailFiles.value.splice(idx - existingCount, 1)
  }
}

function handleSave() {
  if (!form.name || !form.slug || !form.type) return
  emit('save', {
    formData: { ...form, colors: [...form.colors], specs: { ...form.specs }, detailImages: [...form.detailImages] },
    pendingCoverFile: pendingCoverFile.value,
    pendingDetailFiles: [...pendingDetailFiles.value]
  })
}

function resetForm(data) {
  Object.assign(form, data || emptyForm())
  pendingCoverFile.value = null
  pendingDetailFiles.value = []
}

defineExpose({ resetForm })
</script>

<style scoped>
.form-container {
  background: #fff; padding: 2rem; border-radius: 0.75rem; box-shadow: var(--shadow);
}
.form-container h2 {
  color: var(--primary-color); margin-bottom: 1.5rem; font-size: 1.5rem; font-weight: 700;
}
.form-container h3 {
  color: var(--primary-color); margin: 1.75rem 0 1rem;
  border-bottom: 2px solid #f1f5f9; padding-bottom: 0.5rem;
  font-size: 1.1rem; font-weight: 600;
}
.form-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; }
.form-group { display: flex; flex-direction: column; }
.form-group.full-width { grid-column: 1 / -1; }
.form-group label {
  font-weight: 600; color: var(--primary-color); margin-bottom: 0.375rem; font-size: 0.8rem;
}
.form-group input, .form-group select, .form-group textarea {
  padding: 0.625rem 0.75rem; border: 2px solid #e2e8f0; border-radius: 0.5rem;
  font-size: 0.875rem; transition: border-color 0.2s, box-shadow 0.2s;
  font-family: inherit; min-height: 42px;
}
.form-group input:focus, .form-group select:focus, .form-group textarea:focus {
  outline: none; border-color: var(--accent-color);
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}

/* 颜色编辑器 */
.colors-editor { display: flex; flex-wrap: wrap; gap: 0.625rem; align-items: center; }
.color-item {
  display: flex; align-items: center; gap: 0.5rem; background: #f1f5f9;
  padding: 0.375rem 0.75rem; border-radius: 9999px; font-size: 0.8rem; font-weight: 500;
}
.color-swatch {
  width: 24px; height: 24px; border-radius: 50%; border: 2px solid #e2e8f0;
  display: inline-block; flex-shrink: 0;
}
.color-add-row {
  display: flex; gap: 0.5rem; align-items: center; width: 100%; margin-top: 0.5rem;
}
.color-add-row select {
  flex: 1; padding: 0.5rem 0.75rem; border: 2px solid #e2e8f0; border-radius: 0.5rem;
  font-size: 0.875rem; background: #fff; transition: border-color 0.2s, box-shadow 0.2s;
  font-family: inherit; min-height: 42px;
}
.color-add-row select:focus {
  outline: none; border-color: var(--accent-color);
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}
.btn-remove-sm {
  background: #ef4444; color: #fff; border: none; width: 24px; height: 24px;
  border-radius: 50%; cursor: pointer; font-size: 0.75rem;
  display: flex; align-items: center; justify-content: center;
  transition: background 0.2s; flex-shrink: 0;
}
.btn-remove-sm:hover { background: #dc2626; }
.btn-add-color {
  background: #10b981; color: #fff; border: none; padding: 0.5rem 1.25rem;
  border-radius: 9999px; cursor: pointer; font-weight: 600; font-size: 0.875rem;
  white-space: nowrap; transition: all 0.2s; font-family: inherit; min-height: 42px;
}
.btn-add-color:hover:not(:disabled) { background: #059669; transform: translateY(-1px); }
.btn-add-color:disabled { background: #cbd5e1; cursor: not-allowed; }

/* 图片上传 */
.image-upload-section { margin-bottom: 0.75rem; }
.image-upload-section input[type="file"] { font-size: 0.875rem; color: #64748b; font-family: inherit; }
.image-upload-section input[type="file"]::file-selector-button {
  background: var(--accent-color); color: white; border: none; padding: 0.5rem 1rem;
  border-radius: 9999px; font-weight: 600; font-size: 0.8rem; cursor: pointer;
  margin-right: 0.75rem; transition: all 0.2s; font-family: inherit;
}
.image-upload-section input[type="file"]::file-selector-button:hover { background: var(--accent-color-dark); }
.current-cover { margin-bottom: 0.75rem; }
.preview-img {
  max-width: 200px; max-height: 120px; object-fit: cover;
  border-radius: 0.75rem; border: 2px solid #f1f5f9;
}
.detail-images-grid { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-bottom: 0.75rem; }
.detail-img-item { position: relative; }
.preview-img-sm {
  width: 100px; height: 75px; object-fit: cover;
  border-radius: 0.5rem; border: 2px solid #f1f5f9;
}
.detail-img-item .btn-remove-sm { position: absolute; top: -8px; right: -8px; }

/* 表单操作按钮 */
.form-actions {
  display: flex; gap: 0.75rem; margin-top: 2rem;
  padding-top: 1.5rem; border-top: 2px solid #f1f5f9;
}
.btn-save {
  background: #10b981; color: #fff; border: none; padding: 0.75rem 2rem;
  border-radius: 9999px; font-weight: 600; font-size: 1rem; cursor: pointer;
  transition: all 0.2s; font-family: inherit; min-height: 48px;
}
.btn-save:hover { background: #059669; transform: translateY(-1px); box-shadow: var(--shadow); }
.btn-save:disabled { background: #94a3b8; cursor: not-allowed; transform: none; box-shadow: none; }
.btn-cancel {
  background: #64748b; color: #fff; border: none; padding: 0.75rem 2rem;
  border-radius: 9999px; font-weight: 600; font-size: 1rem; cursor: pointer;
  transition: all 0.2s; font-family: inherit; min-height: 48px;
}
.btn-cancel:hover { background: #475569; transform: translateY(-1px); }

@media (max-width: 768px) {
  .form-container { padding: 1.25rem; }
  .form-grid { grid-template-columns: 1fr; }
  .form-actions { flex-direction: column; }
  .form-actions button { width: 100%; }
}
@media (max-width: 480px) {
  .form-container { padding: 1rem; }
  .form-container h2 { font-size: 1.25rem; }
  .detail-images-grid { gap: 0.5rem; }
  .preview-img-sm { width: 72px; height: 54px; }
}
</style>

