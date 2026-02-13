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
    const res = await fetch('https://raw.githubusercontent.com/OUTshipping/OUTshipping.github.io/source/public/data/vehicles.json')
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
    background-color: var(--accent-color);
    color: white;
    padding: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    border: none;
    border-radius: 9999px;
    cursor: pointer;
    box-sizing: border-box;
    font-size: 14px;
    font-weight: 600;
    transition: all 0.2s;
    width: 100%;
    min-width: auto;
    font-family: inherit;
}

.select-selected:hover {
    background-color: var(--accent-color-dark);
    transform: translateY(-1px);
}

.select-items {
    position: absolute;
    top: calc(100% + 5px);
    left: 0;
    width: 100%;
    background-color: var(--card-bg-color);
    border-radius: 0.75rem;
    box-shadow: var(--shadow-lg);
    z-index: 1000;
    border: 1px solid rgba(255, 255, 255, 0.1);
    box-sizing: border-box;
    max-height: 300px;
    overflow-y: auto;
}

.select-items div {
    background-color: transparent;
    color: var(--text-color);
    padding: 10px 16px;
    cursor: pointer;
    transition: background 0.2s;
}

.select-items div:hover {
    background-color: var(--card-hover-color);
    color: var(--accent-color);
}

.filter-btn {
    flex: 1 1 0%;
    display: flex;
    padding: 12px;
    font-size: 14px;
    font-weight: 600;
    color: var(--secondary-color);
    background: linear-gradient(135deg, var(--accent-color) 30%, var(--accent-color-dark) 70%);
    border: none;
    border-radius: 9999px;
    transition: all 0.2s;
    cursor: pointer;
    justify-content: center;
    align-items: center;
    white-space: nowrap;
    margin: 0;
    box-sizing: border-box;
    font-family: inherit;
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
    gap: 1.5rem;
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
    border-radius: 0.75rem;
    box-shadow: var(--shadow);
    transition: transform 0.3s, box-shadow 0.3s;
    width: calc(33.333% - 1.5rem);
    max-width: 340px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    overflow: hidden;
    position: relative;
    text-align: center;
    border: 1px solid rgba(255, 255, 255, 0.05);
}

.vehicle-card:hover {
    transform: translateY(-6px);
    box-shadow: var(--shadow-lg);
}

.vehicle-card img {
    width: 100%;
    height: 200px;
    object-fit: cover;
    transition: transform 0.3s;
}

.vehicle-card:hover img {
    transform: scale(1.05);
}

.card-content {
    padding: 1rem 1.25rem 1.25rem;
    text-align: left;
    width: 100%;
    box-sizing: border-box;
}

.vehicle-card h3 {
    font-size: 1.05rem;
    color: var(--primary-color);
    margin-bottom: 0.5rem;
    text-transform: uppercase;
    font-weight: 700;
    letter-spacing: 0.02em;
}

.info-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 0.25rem;
    margin: 0.5rem 0;
}

.info-item {
    display: flex;
    flex-direction: row;
    align-items: center;
    font-size: 0.8rem;
    margin-bottom: 0.125rem;
    gap: 0.25rem;
}

.info-key {
    display: flex;
    align-items: center;
    font-weight: 600;
    color: var(--accent-color);
    gap: 0.25rem;
}

.info-value {
    font-weight: normal;
    color: #475569;
}

.color-circle-container {
    display: flex;
    gap: 0.375rem;
    margin: 0.75rem 0;
}

.color-circle {
    width: 16px;
    height: 16px;
    border-radius: 50%;
    border: 2px solid var(--primary-color);
    display: inline-block;
}

.btn {
    display: block;
    margin: 0.75rem auto 0;
    width: 160px;
    text-align: center;
    font-size: 0.875rem;
}

.no-vehicle-alert {
    padding: 1.25rem;
    background: #fef2f2;
    border-radius: 0.75rem;
    margin: 1.5rem auto;
    width: 80%;
    text-align: center;
    font-weight: 600;
    color: #991b1b;
    border-left: 4px solid #ef4444;
}

@media (max-width: 768px) {
    .filter-buttons-container {
        flex-direction: column;
        align-items: stretch;
        gap: 0.625rem;
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
        gap: 1rem;
        justify-content: center;
    }

    .vehicle-card {
        width: calc(50% - 1rem);
        max-width: none;
    }

    main {
        padding: 1.25rem 0.75rem;
    }
}

@media (max-width: 480px) {
    .filter-title {
        font-size: 1.1rem;
    }

    .vehicle-section {
        gap: 0.75rem;
    }

    .vehicle-card {
        width: 100%;
        max-width: 340px;
    }

    .vehicle-card img {
        height: 160px;
    }

    main {
        padding: 1rem 0.5rem;
    }
}
</style>

