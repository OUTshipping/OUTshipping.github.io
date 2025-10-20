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
    background: linear-gradient(135deg, var(--primary-color) 0%, #002a54 100%);
    text-align: center;
    min-height: 60vh;
}

.back-link {
    display: inline-block;
    color: var(--secondary-color);
    font-size: 18px;
    margin-bottom: 30px;
    text-decoration: none;
    transition: all 0.3s ease;
    padding: 10px 20px;
    border-radius: 8px;
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
}

.back-link:hover {
    transform: translateX(-5px);
    background: rgba(255, 255, 255, 0.2);
    box-shadow: 0 4px 15px rgba(0, 116, 217, 0.3);
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
    border-radius: 20px;
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.3);
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
    background: linear-gradient(135deg, rgba(0, 116, 217, 0.9), rgba(0, 52, 110, 0.9));
    color: white;
    border: none;
    padding: 18px 22px;
    font-size: 26px;
    cursor: pointer;
    z-index: 2;
    border-radius: 50%;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
    width: 55px;
    height: 55px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.carousel-arrow:hover {
    background: linear-gradient(135deg, rgba(0, 116, 217, 1), rgba(0, 85, 170, 1));
    transform: translateY(-50%) scale(1.1);
    box-shadow: 0 6px 20px rgba(0, 116, 217, 0.5);
}

.carousel-arrow:active {
    transform: translateY(-50%) scale(0.95);
}

.prev-arrow {
    left: 20px;
}

.next-arrow {
    right: 20px;
}

.vehicle-specs {
    text-align: left;
    background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
    padding: 40px;
    border-radius: 20px;
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.15);
    border: 1px solid rgba(0, 116, 217, 0.1);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    min-height: 500px;
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
    color: var(--primary-color);
    font-size: 32px;
    margin-bottom: 20px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: -0.5px;
    background: linear-gradient(135deg, var(--primary-color), var(--accent-color));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.vehicle-description {
    color: #333;
    margin-bottom: 0;
    line-height: 1.8;
    font-size: 16px;
    padding: 20px;
    background: rgba(0, 116, 217, 0.05);
    border-radius: 12px;
    border-left: 4px solid var(--accent-color);
}

.vehicle-specs table {
    width: 100%;
    margin: 0;
    border-collapse: separate;
    border-spacing: 0;
    overflow: hidden;
    border-radius: 12px;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.08);
}

.vehicle-specs tbody {
    border: none;
}

.vehicle-specs th,
.vehicle-specs td {
    padding: 18px 20px;
    text-align: left;
    border: none;
    transition: all 0.3s ease;
    font-size: 15px;
}

.vehicle-specs th {
    background: linear-gradient(135deg, var(--accent-color), #0055aa);
    color: var(--secondary-color);
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    font-size: 14px;
    border-bottom: 2px solid rgba(255, 255, 255, 0.2);
}

.vehicle-specs th i {
    margin-right: 8px;
    opacity: 0.9;
}

.vehicle-specs td {
    color: var(--dark-color);
    background: white;
    font-weight: 500;
}

.vehicle-specs tbody tr {
    border-bottom: 1px solid rgba(0, 0, 0, 0.05);
}

.vehicle-specs tbody tr:last-child {
    border-bottom: none;
}

.vehicle-specs tbody tr:hover {
    background: linear-gradient(90deg, rgba(0, 116, 217, 0.08), rgba(0, 116, 217, 0.03));
    transform: translateX(5px);
}

.vehicle-specs tbody tr:hover td {
    background: transparent;
}

.color-options {
    display: flex;
    gap: 15px;
    margin-top: 0;
    padding: 20px;
    background: rgba(0, 116, 217, 0.05);
    border-radius: 12px;
    align-items: center;
    flex-shrink: 0;
}

.color-options::before {
    content: "Available Colors:";
    font-weight: 600;
    color: var(--primary-color);
    margin-right: 10px;
    font-size: 14px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.color-circle {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    border: 3px solid #e0e0e0;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
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
        gap: 30px;
    }

    main {
        padding: 30px 15px;
    }

    .vehicle-specs {
        padding: 25px 20px;
    }

    .vehicle-specs h2 {
        font-size: 24px;
    }

    .carousel-arrow {
        padding: 12px 15px;
        font-size: 20px;
        width: 45px;
        height: 45px;
    }

    .prev-arrow {
        left: 10px;
    }

    .next-arrow {
        right: 10px;
    }

    .vehicle-specs th,
    .vehicle-specs td {
        padding: 14px 15px;
        font-size: 14px;
    }

    .color-circle {
        width: 35px;
        height: 35px;
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
        font-size: 20px;
    }

    .vehicle-description {
        font-size: 14px;
        padding: 15px;
    }

    .vehicle-specs th,
    .vehicle-specs td {
        padding: 12px 10px;
        font-size: 13px;
    }
}
</style>

