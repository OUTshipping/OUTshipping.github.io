<template>
  <div class="services-page">
    <HeaderNav />
    
    <div class="hero">
      <h1>Our Services</h1>
      <p>More than a dealership — we provide a complete ecosystem of electric mobility solutions in Kigali</p>
    </div>

    <main>
      <h2>What We Offer</h2>
      <div class="service-section">
        <div class="service-item">
          <div class="service-item-content">
            <router-link to="/inventory">
              <div>
                <h3>Car Sales<span class="arrow">→</span></h3>
                <p>Browse our full inventory of brand-new electric and hybrid vehicles from BYD, Dongfeng, and other trusted manufacturers. From compact city sedans to heavy-duty commercial trucks, every vehicle comes with a factory warranty, transparent pricing, and our dedicated after-sales support team to keep you on the road.</p>
              </div>
            </router-link>
          </div>
        </div>
        <div class="service-item">
          <div class="service-item-content">
            <router-link to="/charging">
              <div>
                <h3>EV Charging<span class="arrow">→</span></h3>
                <p>Charge up at our on-site fast-charging station in Kicukiro, Kigali. We support multiple connector standards and offer both AC and DC charging options, so whether you are topping off during a quick visit or need a full charge, we have got you covered. Open to all EV owners — not just our customers.</p>
              </div>
            </router-link>
          </div>
        </div>
        <div class="service-item">
          <div class="service-item-content">
            <router-link to="/taxi">
              <div>
                <h3>Taxi Service<span class="arrow">→</span></h3>
                <p>Experience Kigali in a clean, quiet electric vehicle. Our taxi fleet features well-maintained EVs driven by professional, licensed drivers who know the city inside out. Enjoy air-conditioned comfort, cashless payment options, and the satisfaction of choosing a zero-emission ride for your daily commute or airport transfer.</p>
              </div>
            </router-link>
          </div>
        </div>
        <div class="service-item">
          <div class="service-item-content">
            <router-link to="/rental">
              <div>
                <h3>Car Rental<span class="arrow">→</span></h3>
                <p>Need a vehicle for a day, a week, or longer? Our rental fleet includes a range of electric models suited for business trips, family vacations, or special occasions. Enjoy competitive daily rates, comprehensive insurance options, and the convenience of picking up and dropping off right at our Kigali showroom.</p>
              </div>
            </router-link>
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
import { useHead } from '@unhead/vue'
import HeaderNav from '@/components/HeaderNav.vue'
import FooterBar from '@/components/FooterBar.vue'
import SocialMedia from '@/components/SocialMedia.vue'
import ContactInfo from '@/components/ContactInfo.vue'

useHead({
  title: 'Services — Car Sales, EV Charging, Taxi & Rental | Triple Goats',
  meta: [
    { name: 'description', content: 'Comprehensive automotive services including EV sales, charging stations, electric taxi service and car rental in Kigali.' },
    { property: 'og:title', content: 'Services — Car Sales, EV Charging, Taxi & Rental | Triple Goats' },
    { property: 'og:description', content: 'Comprehensive automotive services including EV sales, charging stations, electric taxi service and car rental in Kigali.' },
    { property: 'og:url', content: 'https://tgautomobile.com/services' },
  ],
  link: [
    { rel: 'canonical', href: 'https://tgautomobile.com/services' }
  ]
})
</script>

<style scoped>
.hero {
    position: relative;
    height: 60vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    color: var(--secondary-color);
    text-align: center;
    background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('/services.jpg');
    background-size: cover;
    background-position: center;
}

.hero h1 {
    font-size: 48px;
    margin-bottom: 20px;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
}

.hero p {
    font-size: 24px;
    margin-bottom: 30px;
}

main {
    padding: 50px 20px;
    background: var(--primary-color);
    text-align: center;
}

main h2 {
    text-align: center;
    margin-bottom: 20px;
}

.service-section {
    display: flex;
    flex-direction: column;
    gap: 30px;
    justify-content: center;
    padding: 50px 20px;
    background: var(--primary-color);
    max-width: 1000px;
    margin: 0 auto;
}

.service-item {
    display: flex;
    align-items: center;
    padding: 25px;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 15px;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s, box-shadow 0.3s;
}

.service-item:hover {
    transform: translateY(-10px);
    box-shadow: 0 12px 30px rgba(0, 0, 0, 0.2);
}

.service-item-content {
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: left;
    margin-left: 15px;
    flex: 1;
}

.service-item-content a {
    display: flex;
    align-items: center;
    color: inherit;
    text-decoration: none;
    width: 100%;
}

.service-item-content a .arrow {
    margin-left: 10px;
    font-size: 22px;
    transition: transform 0.3s;
    color: var(--accent-color);
}

.service-item-content a:hover .arrow {
    transform: translateX(5px);
}

.service-item h3 {
    font-size: 28px;
    color: var(--secondary-color);
    text-align: center;
    margin: 0;
    display: flex;
    align-items: center;
    justify-content: center;
}

.service-item h3 .arrow {
    margin-left: 10px;
    color: var(--accent-color);
}

.service-item p {
    font-size: 18px;
    color: var(--secondary-color);
    line-height: 1.6;
    margin-bottom: 20px;
    opacity: 0.9;
}
</style>

