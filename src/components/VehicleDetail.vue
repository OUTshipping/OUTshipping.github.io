<template>
  <div class="vehicle-detail">
    <HeaderNav />
    
    <main>
      <router-link to="/inventory" class="back-link">＜ back</router-link>
      <div class="vehicle-info">
        <!-- 图片轮播 -->
        <div class="vehicle-images">
          <div class="carousel-container">
            <button class="carousel-arrow prev-arrow" @click="prevSlide" v-show="images.length > 1">&#10094;</button>
            <button class="carousel-arrow next-arrow" @click="nextSlide" v-show="images.length > 1">&#10095;</button>
            <div class="carousel-slide" :style="{ transform: `translateX(-${currentSlide * 100}%)` }">
              <img 
                v-for="(image, index) in images" 
                :key="index"
                :src="image" 
                :alt="`${vehicleName} Image ${index + 1}`" 
                loading="lazy"
              />
            </div>
          </div>
        </div>

        <!-- 车辆规格 -->
        <div class="vehicle-specs">
          <div class="specs-header">
            <h2>{{ vehicleName }}</h2>
            <div class="vehicle-description">
              <p>{{ description }}</p>
            </div>
          </div>
          
          <div class="specs-content">
            <table>
              <tbody>
                <tr>
                  <th><i class="fas fa-calendar-alt"></i> YEAR</th>
                  <td>{{ specs.year }}</td>
                </tr>
                <tr>
                  <th><i class="fas fa-car"></i> MAKE</th>
                  <td>{{ specs.make }}</td>
                </tr>
                <tr>
                  <th><i class="fas fa-car-side"></i> MODEL</th>
                  <td>{{ specs.model }}</td>
                </tr>
                <tr>
                  <th><i class="fas fa-road"></i> RANGE</th>
                  <td>{{ specs.range }} KM</td>
                </tr>
                <tr>
                  <th><i class="fas fa-users"></i> SEATS</th>
                  <td>{{ specs.seats }}</td>
                </tr>
                <tr>
                  <th><i class="fas fa-cogs"></i> CATEGORY</th>
                  <td>{{ specs.category }}</td>
                </tr>
                <tr>
                  <th><i class="fas fa-battery-full"></i> BATTERY CAPACITY</th>
                  <td>{{ specs.batteryCapacity }}</td>
                </tr>
              </tbody>
            </table>
          </div>
          
          <div class="color-options" v-if="colors && colors.length > 0">
            <span 
              v-for="(color, index) in colors" 
              :key="index"
              class="color-circle" 
              :style="{ backgroundColor: color }">
            </span>
          </div>
        </div>
      </div>
    </main>

    <ContactInfo />
    <SocialMedia />
    <FooterBar />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import HeaderNav from './HeaderNav.vue'
import FooterBar from './FooterBar.vue'
import SocialMedia from './SocialMedia.vue'
import ContactInfo from './ContactInfo.vue'

const props = defineProps({
  vehicleName: {
    type: String,
    required: true
  },
  description: {
    type: String,
    required: true
  },
  specs: {
    type: Object,
    required: true
  },
  images: {
    type: Array,
    required: true
  },
  colors: {
    type: Array,
    default: () => []
  }
})

const currentSlide = ref(0)

const nextSlide = () => {
  currentSlide.value = (currentSlide.value + 1) % props.images.length
}

const prevSlide = () => {
  currentSlide.value = (currentSlide.value - 1 + props.images.length) % props.images.length
}
</script>

<style scoped>
main {
    padding: 60px 30px;
    background: var(--bg-color);
    text-align: center;
    min-height: 60vh;
}

.back-link {
    display: inline-block;
    color: var(--accent-color);
    font-size: 1rem;
    margin-bottom: 30px;
    text-decoration: none;
    transition: all 0.3s ease;
    padding: 10px 20px;
    border-radius: 0.5rem;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.08);
}

.back-link:hover {
    transform: translateX(-5px);
    background: rgba(255, 255, 255, 0.1);
    border-color: var(--accent-color);
    box-shadow: 0 4px 15px rgba(0, 116, 217, 0.2);
}

.vehicle-info {
    display: flex;
    gap: 40px;
    max-width: 1400px;
    margin: 0 auto;
    align-items: stretch;
}

.vehicle-images,
.vehicle-specs {
    flex: 1;
    display: flex;
    flex-direction: column;
}

.carousel-container {
    position: relative;
    width: 100%;
    height: 100%;
    min-height: 500px;
    overflow: hidden;
    border-radius: 0.75rem;
    box-shadow: var(--shadow-lg);
    background: #000;
    display: flex;
    align-items: center;
    justify-content: center;
}

.carousel-slide {
    display: flex;
    height: 100%;
    transition: transform 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}

.carousel-slide img {
    min-width: 100%;
    width: 100%;
    height: 100%;
    object-fit: contain;
    display: block;
}

.carousel-arrow {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    color: white;
    border: 1px solid rgba(255, 255, 255, 0.15);
    padding: 0;
    font-size: 1.2rem;
    cursor: pointer;
    z-index: 2;
    border-radius: 50%;
    transition: all 0.3s ease;
    width: 44px;
    height: 44px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.carousel-arrow:hover {
    background: var(--accent-color);
    border-color: var(--accent-color);
    transform: translateY(-50%) scale(1.1);
    box-shadow: 0 4px 15px rgba(0, 116, 217, 0.4);
}

.carousel-arrow:active {
    transform: translateY(-50%) scale(0.95);
}

.prev-arrow {
    left: 16px;
}

.next-arrow {
    right: 16px;
}

.vehicle-specs {
    text-align: left;
    background: var(--card-bg-color);
    padding: 40px;
    border-radius: 0.75rem;
    box-shadow: var(--shadow-lg);
    border: 1px solid rgba(255, 255, 255, 0.08);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.specs-header {
    flex-shrink: 0;
}

.specs-content {
    flex-grow: 1;
    display: flex;
    align-items: center;
}

.vehicle-specs h2 {
    font-size: 1.75rem;
    margin-bottom: 20px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: -0.5px;
    background: linear-gradient(135deg, var(--accent-color), #60a5fa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.vehicle-description {
    color: var(--text-muted);
    margin-bottom: 0;
    line-height: 1.8;
    font-size: 1rem;
    padding: 20px;
    background: rgba(255, 255, 255, 0.03);
    border-radius: 0.75rem;
    border-left: 4px solid var(--accent-color);
}

.vehicle-specs table {
    width: 100%;
    margin: 0;
    border-collapse: separate;
    border-spacing: 0;
    overflow: hidden;
    border-radius: 0.75rem;
    border: 1px solid rgba(255, 255, 255, 0.06);
}

.vehicle-specs tbody {
    border: none;
}

.vehicle-specs th,
.vehicle-specs td {
    padding: 16px 20px;
    text-align: left;
    border: none;
    transition: all 0.3s ease;
    font-size: 0.9rem;
}

.vehicle-specs th {
    background: rgba(255, 255, 255, 0.05);
    color: var(--accent-color);
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    font-size: 0.85rem;
}

.vehicle-specs th i {
    margin-right: 8px;
    opacity: 0.8;
}

.vehicle-specs td {
    color: var(--text-color);
    background: transparent;
    font-weight: 500;
}

.vehicle-specs tbody tr {
    border-bottom: 1px solid rgba(255, 255, 255, 0.06);
}

.vehicle-specs tbody tr:last-child {
    border-bottom: none;
}

.vehicle-specs tbody tr:hover {
    background: rgba(255, 255, 255, 0.04);
}

.color-options {
    display: flex;
    gap: 15px;
    margin-top: 0;
    padding: 20px;
    background: rgba(255, 255, 255, 0.03);
    border-radius: 0.75rem;
    align-items: center;
    flex-shrink: 0;
}

.color-options::before {
    content: "Available Colors:";
    font-weight: 600;
    color: var(--text-muted);
    margin-right: 10px;
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.color-circle {
    width: 36px;
    height: 36px;
    border-radius: 50%;
    border: 3px solid rgba(255, 255, 255, 0.2);
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
    position: relative;
}

.color-circle:hover {
    transform: scale(1.15);
    border-color: var(--accent-color);
    box-shadow: 0 6px 20px rgba(0, 116, 217, 0.4);
}

.color-circle:active {
    transform: scale(1.05);
}

@media (max-width: 768px) {
    .vehicle-info {
        flex-direction: column;
        gap: 1.5rem;
    }

    main {
        padding: 30px 15px;
    }

    .carousel-container {
        min-height: 280px;
    }

    .vehicle-specs {
        padding: 25px 20px;
    }

    .vehicle-specs h2 {
        font-size: 1.35rem;
    }

    .carousel-arrow {
        width: 38px;
        height: 38px;
        font-size: 1rem;
    }

    .prev-arrow { left: 10px; }
    .next-arrow { right: 10px; }

    .vehicle-specs th,
    .vehicle-specs td {
        padding: 12px 14px;
        font-size: 0.8rem;
    }

    .color-circle {
        width: 30px;
        height: 30px;
    }

    .color-options {
        flex-wrap: wrap;
        padding: 15px;
    }

    .color-options::before {
        width: 100%;
        margin-bottom: 5px;
    }
}

@media (max-width: 480px) {
    .vehicle-specs h2 {
        font-size: 1.15rem;
    }

    .vehicle-description {
        font-size: 0.85rem;
        padding: 15px;
    }

    .vehicle-specs th,
    .vehicle-specs td {
        padding: 10px 10px;
        font-size: 0.75rem;
    }
}
</style>

