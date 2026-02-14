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
import { ref, computed, onMounted, watch } from 'vue'
import { useRoute } from 'vue-router'
import { useHead } from '@unhead/vue'
import VehicleDetail from '@/components/VehicleDetail.vue'
import vehiclesData from '../../public/data/vehicles.json'

const route = useRoute()
const vehicle = ref(null)
const loading = ref(true)
const error = ref(null)

// 加载车辆数据（从本地 JSON 同步查找，SSG 构建时可用）
function loadVehicle(slug) {
  if (!slug) return
  loading.value = true
  error.value = null
  vehicle.value = null
  try {
    const found = vehiclesData.find(v => v.slug === slug && v.enabled)
    if (!found) {
      error.value = 'The vehicle you are looking for does not exist or is currently unavailable.'
    } else {
      vehicle.value = found
    }
  } catch (err) {
    error.value = err.message
  } finally {
    loading.value = false
  }
}

// SSG 构建时和客户端首次加载时立即执行
// route.params.slug 在 SSG 渲染时可能为空，从 route.path 中提取 slug 作为 fallback
const initialSlug = route.params.slug || route.path.split('/').filter(Boolean).pop()
loadVehicle(initialSlug)

// 动态 useHead：根据车辆数据响应式更新 head 标签
useHead(computed(() => {
  const v = vehicle.value
  if (!v) {
    return {
      title: 'Vehicle Details — Triple Goats',
      meta: [
        { name: 'description', content: 'View detailed specs, photos and pricing for this electric vehicle at Triple Goats.' },
        { property: 'og:title', content: 'Vehicle Details — Triple Goats' },
        { property: 'og:description', content: 'View detailed specs, photos and pricing for this electric vehicle at Triple Goats.' },
      ]
    }
  }
  const vehicleTitle = `${v.name} — Electric ${v.specs?.category || 'Vehicle'} | Triple Goats`
  const vehicleDesc = v.description || `${v.name} — ${v.range ? v.range + 'km range, ' : ''}${v.seats ? v.seats + '-seat ' : ''}electric ${v.specs?.category || 'vehicle'} available at Triple Goats, Rwanda's premier EV dealer. View specs, photos and pricing.`
  const vehicleImage = v.coverImage ? `https://tgautomobile.com${v.coverImage}` : 'https://tgautomobile.com/companylogo.jpg'
  const vehicleUrl = `https://tgautomobile.com/vehicle/${v.slug}`
  return {
    title: vehicleTitle,
    meta: [
      { name: 'description', content: vehicleDesc },
      { property: 'og:title', content: vehicleTitle },
      { property: 'og:description', content: vehicleDesc },
      { property: 'og:image', content: vehicleImage },
      { property: 'og:url', content: vehicleUrl },
    ],
    link: [
      { rel: 'canonical', href: vehicleUrl }
    ],
    script: [
      {
        type: 'application/ld+json',
        innerHTML: JSON.stringify({
          '@context': 'https://schema.org',
          '@type': 'Product',
          'name': v.name,
          'image': vehicleImage,
          'description': vehicleDesc,
          'brand': { '@type': 'Brand', 'name': v.specs?.make || 'Triple Goats' },
          'category': 'Electric Vehicle',
          'url': vehicleUrl,
          'offers': {
            '@type': 'Offer',
            'availability': 'https://schema.org/InStock',
            'seller': { '@type': 'Organization', 'name': 'Triple Goats' }
          }
        })
      }
    ]
  }
}))

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

