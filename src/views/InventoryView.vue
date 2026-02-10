<template>
  <div class="inventory-page">
    <HeaderNav />
    
    <main id="vehicles">
      <div class="filter-container">
        <div class="filter-title-section">
          <div class="filter-title">
            <i class="fas fa-search filter-icon"></i>
            Sort & Filter Vehicles
          </div>
        </div>
        <div class="filter-buttons-container">
          <div class="custom-select">
            <div class="select-selected" @click="toggleTypeSelect">{{ selectedTypeLabel }}</div>
            <div class="select-items" v-show="typeSelectOpen">
              <div v-for="type in vehicleTypes" :key="type" @click="selectType(type)">
                {{ type.toUpperCase() }}
              </div>
            </div>
          </div>
          <button 
            v-for="filter in sortFilters" 
            :key="filter.value"
            class="filter-btn" 
            :class="{ active: currentSort === filter.value }"
            @click="setSortFilter(filter.value)">
            {{ filter.label }}
          </button>
        </div>
      </div>
      
      <h2>Available Vehicles</h2>
      <div class="no-vehicle-alert" v-show="filteredVehicles.length === 0">
        Sorry, there is no model available now.
      </div>
      
      <div class="vehicle-section">
        <router-link 
          v-for="vehicle in filteredVehicles" 
          :key="vehicle.id"
          :to="vehicle.link" 
          class="vehicle-card">
          <img :src="vehicle.image" :alt="vehicle.name" loading="lazy">
          <div class="card-content">
            <h3>{{ vehicle.name }}</h3>
            <div class="info-grid">
              <div class="info-item">
                <span class="info-key">
                  <i class="fas fa-car icon-type"></i>
                  Type:
                </span>
                <span class="info-value">{{ vehicle.type }}</span>
              </div>
              <div class="info-item">
                <span class="info-key">
                  <i class="fas fa-tachometer-alt icon-range"></i>
                  Range:
                </span>
                <span class="info-value">{{ vehicle.range }} km</span>
              </div>
              <div class="info-item">
                <span class="info-key">
                  <i class="fas fa-chair icon-seats"></i>
                  Seats:
                </span>
                <span class="info-value">{{ vehicle.seats }}</span>
              </div>
              <div class="info-item">
                <span class="info-key">
                  <i class="fas fa-cog icon-configuration"></i>
                  Configuration:
                </span>
                <span class="info-value">{{ vehicle.configuration }}</span>
              </div>
            </div>
            <div class="color-circle-container">
              <span 
                v-for="(color, index) in vehicle.colors" 
                :key="index"
                class="color-circle" 
                :style="{ backgroundColor: color }">
              </span>
            </div>
            <button class="btn">
              <i class="fas fa-eye" style="margin-right:5px;"></i>View
            </button>
          </div>
        </router-link>
      </div>
    </main>

    <ContactInfo />
    <SocialMedia />
    <FooterBar />
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import HeaderNav from '@/components/HeaderNav.vue'
import FooterBar from '@/components/FooterBar.vue'
import SocialMedia from '@/components/SocialMedia.vue'
import ContactInfo from '@/components/ContactInfo.vue'

const route = useRoute()
const router = useRouter()

const vehicleTypes = ref(['ALL TYPES', 'SEDAN', 'SUV', 'PICKUP', 'TRUCK', 'REFRIGERATED', 'BUS', 'VAN'])
const typeSelectOpen = ref(false)
const selectedType = ref('ALL TYPES')
const currentSort = ref('longest-range')

const sortFilters = [
  { value: 'longest-range', label: 'Longest Range' },
  { value: 'shortest-range', label: 'Shortest Range' },
  { value: 'seats-ascending', label: 'Seats Ascending' },
  { value: 'seats-descending', label: 'Seats Descending' }
]

// 车辆数据从 JSON 文件动态加载
const vehicles = ref([])

const selectedTypeLabel = computed(() => selectedType.value)

const filteredVehicles = computed(() => {
  let result = [...vehicles.value]
  
  // 类型筛选
  if (selectedType.value !== 'ALL TYPES') {
    result = result.filter(v => v.type.toUpperCase() === selectedType.value.toUpperCase())
  }
  
  // 排序
  switch (currentSort.value) {
    case 'longest-range':
      result.sort((a, b) => b.range - a.range)
      break
    case 'shortest-range':
      result.sort((a, b) => a.range - b.range)
      break
    case 'seats-ascending':
      result.sort((a, b) => a.seats - b.seats)
      break
    case 'seats-descending':
      result.sort((a, b) => b.seats - a.seats)
      break
  }
  
  return result
})

const toggleTypeSelect = () => {
  typeSelectOpen.value = !typeSelectOpen.value
}

const selectType = (type) => {
  selectedType.value = type
  typeSelectOpen.value = false
  updateUrlParams()
}

const setSortFilter = (filter) => {
  currentSort.value = filter
}

const updateUrlParams = () => {
  const query = {}
  if (selectedType.value !== 'ALL TYPES') {
    query.type = selectedType.value.toLowerCase()
  }
  router.push({ query })
}

// 监听路由变化
watch(() => route.query.type, (newType) => {
  if (newType) {
    selectedType.value = newType.toUpperCase()
  } else {
    selectedType.value = 'ALL TYPES'
  }
}, { immediate: true })

onMounted(async () => {
  // 从 JSON 文件加载车辆数据
  try {
    const res = await fetch('/data/vehicles.json')
    const data = await res.json()
    // 过滤已启用的车辆，并映射字段以兼容模板
    vehicles.value = data
      .filter(v => v.enabled)
      .map(v => ({
        id: v.id,
        name: v.name,
        type: v.type,
        range: v.range,
        seats: v.seats,
        configuration: v.configuration,
        colors: v.colors,
        image: v.coverImage,
        link: `/vehicle/${v.slug}`
      }))
  } catch (err) {
    console.error('加载车辆数据失败:', err)
  }

  // 处理URL参数
  if (route.query.type) {
    selectedType.value = route.query.type.toUpperCase()
  }

  // 点击外部关闭下拉菜单
  document.addEventListener('click', (e) => {
    if (!e.target.closest('.custom-select')) {
      typeSelectOpen.value = false
    }
  })
})
</script>

<style scoped>
main {
    padding: 50px 20px;
    background: var(--primary-color);
    text-align: center;
}

h2 {
    color: var(--secondary-color);
    margin: 20px 0;
}

.filter-container {
    display: flex;
    flex-direction: column;
    gap: 20px;
    width: 94%;
    max-width: 1200px;
    margin: 40px auto;
    padding: 0 3%;
    box-sizing: border-box;
}

.filter-title-section {
    display: flex;
    justify-content: flex-start;
    width: 100%;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

.filter-title {
    font-size: 24px;
    font-weight: bold;
    color: var(--secondary-color);
    margin-right: 20px;
    text-shadow: 0px 2px 4px rgba(0, 0, 0, 0.3);
    position: relative;
}

.filter-title::before {
    content: '';
    width: 40px;
    height: 4px;
    background: linear-gradient(135deg, var(--accent-color), var(--accent-color-dark));
    border-radius: 4px;
    position: absolute;
    left: 0;
    bottom: -8px;
    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.4);
}

.filter-icon {
    margin-right: 10px;
}

.filter-buttons-container {
    display: flex;
    gap: 12px;
    padding: 15px 20px;
    background: linear-gradient(135deg, rgba(255,255,255,0.05), rgba(255,255,255,0.05));
    border-radius: 8px;
    box-shadow: inset 0 0 8px rgba(0, 0, 0, 0.1);
    width: 94%;
    max-width: 1200px;
    margin: 0 auto;
    align-items: center;
    justify-content: space-between;
    box-sizing: border-box;
}

.custom-select {
    position: relative;
    flex: 1 1 0%;
    min-width: 160px;
    display: flex;
    flex-direction: column;
    margin: 0;
    padding: 0;
    width: 100%;
    box-sizing: border-box;
}

.select-selected {
    background-color: #0055aa;
    color: white;
    padding: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    box-sizing: border-box;
    font-size: 14px;
    font-weight: bold;
    transition: all 0.3s;
    width: 100%;
    min-width: auto;
}

.select-items {
    position: absolute;
    top: calc(100% + 5px);
    left: 0;
    width: 100%;
    background-color: white;
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    z-index: 1000;
    border: 1px solid rgba(0,0,0,0.1);
    box-sizing: border-box;
    max-height: 300px;
    overflow-y: auto;
}

.select-items div {
    background-color: white;
    color: var(--dark-color);
    padding: 10px;
    cursor: pointer;
}

.select-items div:hover {
    background-color: #e7e7e7;
}

.filter-btn {
    flex: 1 1 0%;
    display: flex;
    padding: 12px;
    font-size: 14px;
    font-weight: bold;
    color: var(--secondary-color);
    background: linear-gradient(135deg, var(--accent-color) 30%, var(--accent-color-dark) 70%);
    border: none;
    border-radius: 8px;
    transition: all 0.3s;
    cursor: pointer;
    justify-content: center;
    align-items: center;
    white-space: nowrap;
    margin: 0;
    box-sizing: border-box;
}

.filter-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.2);
}

.filter-btn.active {
    box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.4);
}

.vehicle-section {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    justify-content: center;
    padding: 0 15px;
    background: var(--primary-color);
    width: 100%;
    max-width: 1200px;
    margin: 0 auto;
    box-sizing: border-box;
}

.vehicle-card {
    background: var(--secondary-color);
    border-radius: 15px;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s, box-shadow 0.3s, background-color 0.3s;
    width: calc(33% - 30px);
    max-width: 300px;
    margin: 10px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    padding-bottom: 15px;
    overflow: hidden;
    position: relative;
    text-align: center;
    border: 2px solid transparent;
}

.vehicle-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 12px 30px rgba(0, 0, 0, 0.2);
}

.vehicle-card img {
    width: 100%;
    height: 180px;
    object-fit: cover;
    border-radius: 10px;
    margin-bottom: 10px;
    transition: transform 0.3s;
}

.vehicle-card:hover img {
    transform: scale(1.05);
}

.card-content {
    padding: 15px;
    text-align: left;
    width: 100%;
}

.vehicle-card h3 {
    font-size: 18px;
    color: var(--dark-color);
    margin-bottom: 8px;
    text-transform: uppercase;
    font-weight: bold;
}

.info-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 2px;
    margin: 5px 0;
}

.info-item {
    display: flex;
    flex-direction: row;
    align-items: center;
    font-size: 13px;
    margin-bottom: 2px;
    gap: 5px;
}

.info-key {
    display: flex;
    align-items: center;
    font-weight: bold;
    color: var(--accent-color);
    gap: 5px;
}

.info-value {
    font-weight: normal;
    color: var(--dark-color);
}

.color-circle-container {
    display: flex;
    gap: 5px;
    margin: 10px 0;
}

.color-circle {
    width: 15px;
    height: 15px;
    border-radius: 50%;
    border: 2px solid #001f3f;
    display: inline-block;
}

.btn {
    display: block;
    margin: 20px auto;
    width: 180px;
    text-align: center;
}

.no-vehicle-alert {
    padding: 20px;
    background-color: #ffcccc;
    border-radius: 8px;
    margin: 20px auto;
    width: 80%;
    text-align: center;
    font-weight: bold;
    color: #660000;
}

@media (max-width: 768px) {
    .filter-buttons-container {
        flex-direction: column;
        align-items: stretch;
        gap: 10px;
    }

    .custom-select,
    .filter-btn {
        width: 100%;
        margin: 0;
        padding: 12px;
        font-size: 14px;
        min-width: auto;
        flex: 1 1 auto;
        box-sizing: border-box;
    }

    .vehicle-section {
        flex-wrap: wrap;
        justify-content: flex-start;
        gap: 10px;
    }

    .vehicle-card {
        width: 100%;
        max-width: 300px;
        margin: 10px 0;
    }

    main {
        padding: 20px 10px;
    }
}
</style>

