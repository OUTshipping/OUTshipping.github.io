<template>
  <div v-if="loading" class="loading-container">
    <div class="loading-spinner"></div>
    <p>Loading...</p>
  </div>
  <div v-else-if="error" class="error-container">
    <h2>Vehicle Not Found</h2>
    <p>{{ error }}</p>
    <router-link to="/inventory" class="back-link">Back to Inventory</router-link>
  </div>
  <VehicleDetail
    v-else-if="vehicle"
    :vehicleName="vehicle.name"
    :description="vehicle.description"
    :specs="{
      year: vehicle.specs.year,
      make: vehicle.specs.make,
      model: vehicle.specs.model,
      range: String(vehicle.range),
      seats: String(vehicle.seats),
      category: vehicle.specs.category,
      batteryCapacity: vehicle.specs.batteryCapacity
    }"
    :images="vehicle.detailImages"
    :colors="vehicle.colors"
  />
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { useRoute } from 'vue-router'
import VehicleDetail from '@/components/VehicleDetail.vue'

const route = useRoute()
const vehicle = ref(null)
const loading = ref(true)
const error = ref(null)

// 加载车辆数据
async function loadVehicle(slug) {
  loading.value = true
  error.value = null
  vehicle.value = null
  try {
    const res = await fetch('https://raw.githubusercontent.com/OUTshipping/OUTshipping.github.io/source/public/data/vehicles.json')
    if (!res.ok) throw new Error('无法加载车辆数据')
    const vehicles = await res.json()
    const found = vehicles.find(v => v.slug === slug && v.enabled)
    if (!found) {
      error.value = 'The vehicle you are looking for does not exist or is currently unavailable.'
    } else {
      vehicle.value = found
      // 动态更新页面 SEO 信息
      const vehicleTitle = `${found.name} — Electric ${found.specs?.category || 'Vehicle'} | Triple Goats`
      const vehicleDesc = found.description || `View specs, photos and pricing for the ${found.name} at Triple Goats, Rwanda's premier EV dealer.`
      const vehicleImage = found.image ? `https://tgautomobile.com${found.image}` : 'https://tgautomobile.com/companylogo.jpg'
      document.title = vehicleTitle
      const descTag = document.querySelector('meta[name="description"]')
      if (descTag) descTag.setAttribute('content', vehicleDesc)
      const ogTitle = document.querySelector('meta[property="og:title"]')
      if (ogTitle) ogTitle.setAttribute('content', vehicleTitle)
      const ogDesc = document.querySelector('meta[property="og:description"]')
      if (ogDesc) ogDesc.setAttribute('content', vehicleDesc)
      const ogImage = document.querySelector('meta[property="og:image"]')
      if (ogImage) ogImage.setAttribute('content', vehicleImage)
      const ogUrl = document.querySelector('meta[property="og:url"]')
      if (ogUrl) ogUrl.setAttribute('content', `https://tgautomobile.com/vehicle/${slug}`)
    }
  } catch (err) {
    error.value = err.message
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  loadVehicle(route.params.slug)
})

// 监听路由参数变化，支持同页面内跳转
watch(() => route.params.slug, (newSlug) => {
  if (newSlug) {
    loadVehicle(newSlug)
  }
})
</script>

<style scoped>
.loading-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 60vh;
  color: var(--dark-color);
}

.loading-spinner {
  width: 40px;
  height: 40px;
  border: 4px solid #e0e0e0;
  border-top: 4px solid var(--accent-color);
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.error-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 60vh;
  color: var(--dark-color);
  text-align: center;
  padding: 20px;
}

.error-container h2 {
  font-size: 28px;
  margin-bottom: 10px;
  color: var(--primary-color);
}

.error-container p {
  font-size: 16px;
  margin-bottom: 20px;
  color: #666;
}

.back-link {
  display: inline-block;
  padding: 10px 24px;
  background: var(--accent-color);
  color: #fff;
  border-radius: 6px;
  text-decoration: none;
  transition: background 0.3s;
}

.back-link:hover {
  background: var(--primary-color);
}
</style>

