<template>
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
          <option v-for="m in currentModels" :key="m.nameEn" :value="m.nameEn">
            {{ m.nameEn }}
          </option>
        </select>
      </div>
      <div class="db-selector-group">
        <label>Variant</label>
        <select v-model="selectedVariant" :disabled="!selectedModel">
          <option value="">-- Select Variant --</option>
          <option v-for="v in currentVariants" :key="v.specNameEn" :value="v.specNameEn">
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
</template>

<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
  brandsData: { type: Array, required: true },
  brandsLoading: { type: Boolean, default: false }
})

const emit = defineEmits(['apply-variant'])

const selectedBrand = ref('')
const selectedModel = ref('')
const selectedVariant = ref('')

const currentModels = computed(() => {
  const brand = props.brandsData.find(b => b.nameEn === selectedBrand.value)
  return brand ? brand.models : []
})

const currentVariants = computed(() => {
  const model = currentModels.value.find(m => m.nameEn === selectedModel.value)
  return model ? model.variants : []
})

function onBrandChange() {
  selectedModel.value = ''
  selectedVariant.value = ''
}

function onModelChange() {
  selectedVariant.value = ''
}

function applyVariant() {
  if (!selectedVariant.value) return
  const brand = props.brandsData.find(b => b.nameEn === selectedBrand.value)
  if (!brand) return
  const model = brand.models.find(m => m.nameEn === selectedModel.value)
  if (!model) return
  const variant = model.variants.find(v => v.specNameEn === selectedVariant.value)
  if (!variant) return

  emit('apply-variant', {
    name: `${variant.year} ${brand.nameEn} ${model.nameEn}`,
    type: variant.type || 'SUV',
    range: variant.range || 0,
    seats: variant.seats || 5,
    year: variant.year || '2025',
    make: brand.nameEn,
    model: model.nameEn,
    batteryCapacity: variant.batteryCapacity || 'N/A'
  })
}
</script>

<style scoped>
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
.db-selector-hint { color: #64748b; font-size: 0.8rem; margin: 0 0 1rem 0; }
.db-selector-row { display: flex; gap: 0.75rem; align-items: flex-end; flex-wrap: wrap; }
.db-selector-group { display: flex; flex-direction: column; flex: 1; min-width: 160px; }
.db-selector-group label {
  font-weight: 600; color: var(--primary-color); margin-bottom: 0.375rem; font-size: 0.8rem;
}
.db-selector-group select {
  padding: 0.5rem 0.75rem; border: 2px solid #e2e8f0; border-radius: 0.5rem;
  font-size: 0.875rem; background: #fff; transition: border-color 0.2s, box-shadow 0.2s;
  font-family: inherit; min-height: 42px;
}
.db-selector-group select:focus {
  outline: none; border-color: var(--accent-color);
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}
.db-selector-group select:disabled { background: #f8fafc; color: #94a3b8; cursor: not-allowed; }
.btn-apply-variant {
  padding: 0.5rem 1.5rem; background: var(--accent-color); color: #fff; border: none;
  border-radius: 9999px; font-size: 0.875rem; font-weight: 600; cursor: pointer;
  transition: all 0.2s; white-space: nowrap; align-self: flex-end;
  font-family: inherit; min-height: 42px;
}
.btn-apply-variant:hover:not(:disabled) { background: var(--accent-color-dark); transform: translateY(-1px); }
.btn-apply-variant:disabled { background: #cbd5e1; cursor: not-allowed; }

@media (max-width: 768px) {
  .db-selector-row { flex-direction: column; }
  .db-selector-group { min-width: 100%; }
}
@media (max-width: 480px) {
  .db-selector-card { padding: 1rem; }
}
</style>

