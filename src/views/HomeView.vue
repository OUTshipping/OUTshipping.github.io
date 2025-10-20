<template>
  <div class="home-page">
    <HeaderNav />
    
    <div class="hero">
      <video autoplay muted loop preload="auto">
        <source src="/movie.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <nav class="vehicle-list">
        <router-link to="/inventory?type=sedan">SEDAN</router-link>
        <router-link to="/inventory?type=suv">SUV</router-link>
        <router-link to="/inventory?type=pickup">PICKUP</router-link>
        <router-link to="/inventory?type=truck">TRUCK</router-link>
        <router-link to="/inventory?type=refrigerated">REFRIGERATED</router-link>
        <router-link to="/inventory?type=bus">BUS</router-link>
        <router-link to="/inventory?type=van">VAN</router-link>
      </nav>
    </div>

    <section class="vehicle-section">
      <div class="vehicle-card">
        <img src="/sedan.jpg" alt="Sedan">
        <h3>Sedan</h3>
        <p>Stylish and fuel-efficient sedans for everyday use.</p>
        <router-link to="/inventory?type=sedan" class="btn">
          <i class="fas fa-eye" style="margin-right:5px;"></i>View
        </router-link>
      </div>
      <div class="vehicle-card">
        <img src="/suv.jpg" alt="SUV">
        <h3>SUV</h3>
        <p>Explore our wide range of high-performance SUVs.</p>
        <router-link to="/inventory?type=suv" class="btn">
          <i class="fas fa-eye" style="margin-right:5px;"></i>View
        </router-link>
      </div>
      <div class="vehicle-card">
        <img src="/pickup.jpg" alt="Pickup">
        <h3>Pickup</h3>
        <p>Powerful and reliable pickups to meet all your needs.</p>
        <router-link to="/inventory?type=pickup" class="btn">
          <i class="fas fa-eye" style="margin-right:5px;"></i>View
        </router-link>
      </div>
      <div class="vehicle-card">
        <img src="/truck.jpg" alt="Truck">
        <h3>Truck</h3>
        <p>High-capacity trucks suitable for long-distance transportation.</p>
        <router-link to="/inventory?type=truck" class="btn">
          <i class="fas fa-eye" style="margin-right:5px;"></i>View
        </router-link>
      </div>
      <div class="vehicle-card">
        <img src="/refrigerated.jpg" alt="Refrigerated">
        <h3>Refrigerated</h3>
        <p>Refrigerated vehicles for transporting perishable goods.</p>
        <router-link to="/inventory?type=refrigerated" class="btn">
          <i class="fas fa-eye" style="margin-right:5px;"></i>View
        </router-link>
      </div>
      <div class="vehicle-card">
        <img src="/bus.jpg" alt="Bus">
        <h3>Bus</h3>
        <p>Comfortable and spacious buses for group transportation.</p>
        <router-link to="/inventory?type=bus" class="btn">
          <i class="fas fa-eye" style="margin-right:5px;"></i>View
        </router-link>
      </div>
      <div class="vehicle-card">
        <img src="/van.jpg" alt="Van">
        <h3>Van</h3>
        <p>Efficient and economical vans to support your business.</p>
        <router-link to="/inventory?type=van" class="btn">
          <i class="fas fa-eye" style="margin-right:5px;"></i>View
        </router-link>
      </div>
    </section>

    <div class="map-container">
      <div class="map-header">
        <h2>Find Us on the Map</h2>
        <p class="map-subtitle">Discover Our Convenient Location</p>
      </div>
      <iframe 
        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3987.418287609195!2d30.098935373674106!3d-1.9874280979946188!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x19dcb909c976d39b%3A0x85b1db1ad0e495c5!2z5Y-B576K5rG96L2mIFRnIEVsZWN0cmljIENhciBNYXJrZXQ!5e0!3m2!1szh-CN!2srw!4v1739448007802!5m2!1szh-CN!2srw" 
        width="100%" 
        height="450" 
        style="width: 100%; border: 0;" 
        allowfullscreen="" 
        loading="lazy" 
        referrerpolicy="no-referrer-when-downgrade">
      </iframe>
    </div>

    <ContactInfo />
    <SocialMedia />
    <FooterBar />
  </div>
</template>

<script setup>
import HeaderNav from '@/components/HeaderNav.vue'
import FooterBar from '@/components/FooterBar.vue'
import SocialMedia from '@/components/SocialMedia.vue'
import ContactInfo from '@/components/ContactInfo.vue'
</script>

<style scoped>
.hero {
    position: relative;
    height: 80vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    color: var(--secondary-color);
    text-align: center;
    background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('/hero-bg.jpg');
    background-size: cover;
    background-position: center;
}

.hero video {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    z-index: -1;
    pointer-events: none;
}

.vehicle-list {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background: rgba(0, 31, 63, 0.8);
    padding: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 20px;
    flex-wrap: nowrap;
    z-index: 1000;
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
}

.vehicle-list a {
    color: var(--secondary-color);
    font-size: 18px;
    font-weight: bold;
    padding: 10px 20px;
    border-radius: 5px;
    text-decoration: none;
    transition: background-color 0.3s, transform 0.3s;
    margin: 0 10px;
}

.vehicle-list a:hover {
    text-decoration: underline;
    background: rgba(255, 255, 255, 0.2);
    transform: scale(1.1);
    margin: 0 5px;
}

.vehicle-section {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 20px;
    padding: 20px;
}

.vehicle-card {
    background: var(--card-bg-color);
    border-radius: 15px;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s, box-shadow 0.3s, background-color 0.3s;
    padding-bottom: 20px;
    overflow: hidden;
    position: relative;
    text-align: center;
}

.vehicle-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 12px 25px rgba(0, 0, 0, 0.2);
    background-color: var(--card-hover-color);
}

.vehicle-card img {
    width: 100%;
    height: 200px;
    object-fit: cover;
    border-radius: 10px;
    transition: transform 0.3s;
}

.vehicle-card:hover img {
    transform: scale(1.05);
}

.vehicle-card h3 {
    font-size: 20px;
    color: var(--text-color);
    margin: 10px 0;
    text-transform: uppercase;
}

.vehicle-card p {
    font-size: 14px;
    line-height: 1.5;
    color: var(--text-color);
    margin: 10px 0;
}

.map-container {
    padding: 30px 0;
    background: var(--primary-color);
    text-align: center;
    margin: 40px 0;
}

.map-header {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin-bottom: 20px;
}

.map-header h2 {
    font-size: 24px;
    margin-bottom: 8px;
}

.map-header .map-subtitle {
    font-size: 16px;
    color: var(--secondary-color);
}

@media (max-width: 768px) {
    .vehicle-section {
        grid-template-columns: 1fr;
        gap: 10px;
    }

    .vehicle-card img {
        height: 250px;
    }

    .hero {
        height: 40vh;
    }

    .hero video {
        height: 100%;
    }

    .vehicle-list {
        display: none;
    }

    .map-content {
        margin: 30px 0;
        height: 350px;
    }
}
</style>

