<template>
  <div class="home-page">
    <HeaderNav />

    <!-- Hero Section -->
    <div class="hero">
      <video autoplay muted loop playsinline class="hero-video">
        <source src="/movie.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <div class="hero-overlay"></div>
      <div class="hero-content container">
        <h1>驾驭未来出行</h1>
        <p>优质电动汽车，驶向绿色明天</p>
        <div class="hero-actions">
          <router-link to="/inventory" class="btn btn-primary">浏览库存</router-link>
          <router-link to="/testdrive" class="btn btn-outline">预约试驾</router-link>
        </div>
      </div>
    </div>

    <!-- Quick Vehicle Categories -->
    <div class="category-strip">
      <div class="container category-grid">
        <router-link to="/inventory?type=sedan" class="category-item">
            <i class="fas fa-car-side"></i> 轿车
        </router-link>
        <router-link to="/inventory?type=suv" class="category-item">
            <i class="fas fa-shuttle-van"></i> SUV
        </router-link>
        <router-link to="/inventory?type=pickup" class="category-item">
            <i class="fas fa-truck-pickup"></i> 皮卡
        </router-link>
        <router-link to="/inventory?type=truck" class="category-item">
            <i class="fas fa-truck"></i> 卡车
        </router-link>
        <router-link to="/inventory?type=bus" class="category-item">
            <i class="fas fa-bus"></i> 巴士
        </router-link>
        <router-link to="/inventory?type=van" class="category-item">
            <i class="fas fa-shipping-fast"></i> 厢式车
        </router-link>
      </div>
    </div>

    <!-- Featured Vehicles -->
    <section class="section container">
      <div class="section-header">
        <h2>精选车型</h2>
        <p>探索我们评价最高的电动汽车，兼具性能与舒适。</p>
      </div>

      <div class="vehicle-grid">
        <div class="vehicle-card">
          <div class="card-image">
            <img src="/sedan.jpg" alt="Sedan" loading="lazy">
            <span class="badge">热销</span>
          </div>
          <div class="card-content">
            <h3>轿车</h3>
            <p>高效、时尚，城市出行的完美选择。体验平稳加速与静谧舒适。</p>
            <router-link to="/inventory?type=sedan" class="btn btn-sm">查看详情</router-link>
          </div>
        </div>

        <div class="vehicle-card">
          <div class="card-image">
            <img src="/suv.jpg" alt="SUV" loading="lazy">
          </div>
          <div class="card-content">
            <h3>SUV</h3>
            <p>宽敞且强劲。先进安全配置，家庭与探险的理想之选。</p>
            <router-link to="/inventory?type=suv" class="btn btn-sm">查看详情</router-link>
          </div>
        </div>

        <div class="vehicle-card">
          <div class="card-image">
            <img src="/pickup.jpg" alt="Pickup" loading="lazy">
          </div>
          <div class="card-content">
            <h3>皮卡</h3>
            <p>强悍性能与电动效率的完美结合，工作与休闲兼备。</p>
            <router-link to="/inventory?type=pickup" class="btn btn-sm">查看详情</router-link>
          </div>
        </div>

        <!-- Add more cards as needed -->
         <div class="vehicle-card">
            <div class="card-image">
              <img src="/truck.jpg" alt="Truck" loading="lazy">
            </div>
            <div class="card-content">
              <h3>卡车</h3>
              <p>商用重载性能，可靠且经济高效。</p>
              <router-link to="/inventory?type=truck" class="btn btn-sm">查看详情</router-link>
            </div>
          </div>

          <div class="vehicle-card">
            <div class="card-image">
              <img src="/refrigerated.jpg" alt="Refrigerated" loading="lazy">
            </div>
            <div class="card-content">
              <h3>冷藏车</h3>
              <p>精准温控，确保易腐货物的新鲜品质。</p>
              <router-link to="/inventory?type=refrigerated" class="btn btn-sm">查看详情</router-link>
            </div>
          </div>

          <div class="vehicle-card">
            <div class="card-image">
              <img src="/bus.jpg" alt="Bus" loading="lazy">
            </div>
            <div class="card-content">
              <h3>巴士</h3>
              <p>清洁公共交通解决方案，大容量舒适座椅。</p>
              <router-link to="/inventory?type=bus" class="btn btn-sm">查看详情</router-link>
            </div>
          </div>

           <div class="vehicle-card">
            <div class="card-image">
              <img src="/van.jpg" alt="Van" loading="lazy">
            </div>
            <div class="card-content">
              <h3>厢式车</h3>
              <p>灵活货运空间，物流配送的得力助手。</p>
              <router-link to="/inventory?type=van" class="btn btn-sm">查看详情</router-link>
            </div>
          </div>
      </div>
    </section>

    <!-- Map Section -->
    <section class="map-section">
      <div class="container">
        <div class="section-header">
            <h2>参观我们的展厅</h2>
            <p>欢迎亲临我们的展厅，实地体验我们的车辆。</p>
        </div>
        <div class="map-container">
            <iframe
            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3987.418287609195!2d30.098935373674106!3d-1.9874280979946188!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x19dcb909c976d39b%3A0x85b1db1ad0e495c5!2z5Y-B576K5rG96L2mIFRnIEVsZWN0cmljIENhciBNYXJrZXQ!5e0!3m2!1szh-CN!2srw!4v1739448007802!5m2!1szh-CN!2srw"
            width="100%"
            height="450"
            style="border:0;"
            allowfullscreen=""
            loading="lazy"
            referrerpolicy="no-referrer-when-downgrade">
            </iframe>
        </div>
      </div>
    </section>

    <ContactInfo />
    <FooterBar />
  </div>
</template>

<script setup>
import HeaderNav from '@/components/HeaderNav.vue'
import FooterBar from '@/components/FooterBar.vue'
import ContactInfo from '@/components/ContactInfo.vue'
</script>

<style scoped>
.hero {
    position: relative;
    height: 90vh;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    margin-top: -80px; /* Offset fixed header if transparent, or just overlap */
}

.hero-video {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    z-index: -1;
}

.hero-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(to bottom, rgba(15, 23, 42, 0.4), rgba(15, 23, 42, 0.8));
    z-index: 0;
}

.hero-content {
    position: relative;
    z-index: 1;
    text-align: center;
    color: white;
    max-width: 800px;
}

.hero h1 {
    font-size: 3.5rem;
    font-weight: 800;
    margin-bottom: 1.5rem;
    line-height: 1.2;
    text-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
}

.hero p {
    font-size: 1.25rem;
    margin-bottom: 2.5rem;
    color: var(--secondary-color);
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

.hero-actions {
    display: flex;
    gap: 1rem;
    justify-content: center;
}

.btn-primary {
    background-color: var(--accent-color);
    color: white;
}

.btn-primary:hover {
    background-color: var(--accent-color-dark);
}

.btn-outline {
    background-color: transparent;
    border: 2px solid white;
    color: white;
}

.btn-outline:hover {
    background-color: white;
    color: var(--primary-color);
}

/* Category Strip */
.category-strip {
    background-color: var(--card-bg-color);
    padding: 2rem 0;
    border-bottom: 1px solid rgba(255,255,255,0.05);
}

.category-grid {
    display: flex;
    justify-content: center;
    gap: 1.5rem;
    flex-wrap: wrap;
}

.category-item {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.75rem 1.5rem;
    background: rgba(255, 255, 255, 0.05);
    border-radius: 0.5rem;
    color: var(--text-color);
    font-weight: 600;
    transition: all 0.3s ease;
    text-decoration: none;
}

.category-item:hover {
    background: var(--accent-color);
    color: white;
    transform: translateY(-2px);
}

/* Sections */
.section {
    padding: 5rem 0;
}

.section-header {
    text-align: center;
    margin-bottom: 4rem;
}

.section-header h2 {
    font-size: 2.5rem;
    color: var(--text-color);
    margin-bottom: 1rem;
}

.section-header p {
    color: var(--text-muted);
    font-size: 1.1rem;
}

/* Vehicle Grid */
.vehicle-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 2rem;
}

.vehicle-card {
    background: var(--card-bg-color);
    border-radius: 1rem;
    overflow: hidden;
    box-shadow: var(--shadow);
    transition: all 0.3s ease;
    border: 1px solid rgba(255, 255, 255, 0.05);
    display: flex;
    flex-direction: column;
}

.vehicle-card:hover {
    transform: translateY(-5px);
    box-shadow: var(--shadow-lg);
    border-color: var(--accent-color);
}

.card-image {
    position: relative;
    height: 220px;
    overflow: hidden;
}

.card-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.5s ease;
}

.vehicle-card:hover .card-image img {
    transform: scale(1.1);
}

.badge {
    position: absolute;
    top: 1rem;
    right: 1rem;
    background: var(--accent-color);
    color: white;
    padding: 0.25rem 0.75rem;
    border-radius: 9999px;
    font-size: 0.75rem;
    font-weight: 700;
    text-transform: uppercase;
    box-shadow: 0 2px 4px rgba(0,0,0,0.2);
}

.card-content {
    padding: 1.5rem;
    flex-grow: 1;
    display: flex;
    flex-direction: column;
}

.card-content h3 {
    font-size: 1.5rem;
    color: white;
    margin-bottom: 0.5rem;
}

.card-content p {
    color: var(--text-muted);
    font-size: 0.95rem;
    margin-bottom: 1.5rem;
    line-height: 1.5;
    flex-grow: 1;
}

.btn-sm {
    padding: 0.5rem 1.25rem;
    font-size: 0.9rem;
    align-self: flex-start;
}

/* Map Section */
.map-section {
    background: var(--primary-color);
    padding-bottom: 5rem;
}

.map-container {
    border-radius: 1rem;
    overflow: hidden;
    box-shadow: var(--shadow-lg);
    border: 1px solid rgba(255, 255, 255, 0.1);
}

/* Responsive */
@media (max-width: 768px) {
    .hero h1 {
        font-size: 2.5rem;
    }

    .hero-actions {
        flex-direction: column;
    }

    .category-grid {
        justify-content: flex-start;
        overflow-x: auto;
        padding-bottom: 1rem;
        flex-wrap: nowrap;
    }

    .category-item {
        flex-shrink: 0;
    }

    .section {
        padding: 3rem 0;
    }
}
</style>

