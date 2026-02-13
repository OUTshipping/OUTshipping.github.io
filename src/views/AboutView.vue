<template>
  <div class="about-page">
    <HeaderNav />
    
    <div class="hero">
      <h1>About T&G AUTOMOBILE</h1>
      <p>Driving Rwanda's electric future — one vehicle at a time</p>
    </div>

    <main>
      <h2>Who We Are</h2>
      <div class="about-section">
        <div class="section">
          <div class="section-content">
            <h3>Our Mission</h3>
            <p>Triple Goats — officially San Yang (Rwanda) Automobile Sales Co., Ltd. — is on a mission to make clean, affordable transportation accessible to everyone in Rwanda. We partner directly with leading Chinese EV manufacturers including BYD and Dongfeng to bring a full spectrum of new energy vehicles to East Africa: compact city sedans, family SUVs, rugged pickups, commercial trucks, refrigerated vehicles, buses, and vans. Whether you are an individual buyer, a fleet operator, or a government agency, we provide end-to-end support from vehicle selection and financing guidance to after-sales maintenance and genuine spare parts.</p>
          </div>
        </div>
        <div class="section">
          <div class="section-content">
            <h3>Our Values</h3>
            <p>Everything we do is built on three pillars: transparency, expertise, and customer-first thinking. We publish honest specifications and real-world range data so you can make confident decisions. Our bilingual sales team (English, French, Kinyarwanda, and Chinese) is trained on every model we carry, ready to explain battery technology, charging options, and total cost of ownership. We do not just sell cars — we stay with you for the lifetime of your vehicle, offering scheduled maintenance, warranty support, and 24/7 roadside assistance in the Kigali area.</p>
          </div>
        </div>
        <div class="section">
          <div class="section-content">
            <h3>Our Story</h3>
            <p>Founded in 2023 in Kigali's Kicukiro district, Triple Goats started with a simple observation: Rwanda's ambitious green-growth targets needed a reliable local partner to supply quality electric vehicles. In just two years we have grown from a single showroom to a full-service operation with a dedicated EV charging station, a professional service center, and a growing network of satisfied customers across the country. Our rapid growth reflects both the rising demand for EVs in Africa and the trust our customers place in us.</p>
          </div>
        </div>
        <div class="section">
          <div class="section-content">
            <h3>Community &amp; Sustainability</h3>
            <p>We believe selling electric vehicles is only part of the solution. That is why we invest in EV awareness campaigns, partner with local driving schools to offer electric-vehicle training modules, and sponsor road safety programs in Kigali schools. We are also working toward installing public charging points beyond our showroom to help build the infrastructure Rwanda needs for widespread EV adoption. Every vehicle we put on the road is one less source of tailpipe emissions — and we are proud to play our part in Rwanda's vision of a cleaner, greener future.</p>
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
import HeaderNav from '@/components/HeaderNav.vue'
import FooterBar from '@/components/FooterBar.vue'
import SocialMedia from '@/components/SocialMedia.vue'
import ContactInfo from '@/components/ContactInfo.vue'
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
    background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('/about.jpg');
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
    text-align: left;
    padding-left: 20px;
}

.about-section {
    display: flex;
    flex-direction: column;
    gap: 30px;
    justify-content: center;
    padding: 50px 20px;
    background: var(--primary-color);
}

.section {
    background-color: #f5f5f5;
    padding: 2rem;
    margin: 2rem 0;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.section-content {
    background-color: #ffffff;
    padding: 1.5rem;
    border-radius: 8px;
    box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.05);
}

.section h3 {
    color: #2c3e50;
    font-size: 32px;
    margin: 0 0 1rem;
    border-bottom: 2px solid #0074d9;
    padding-bottom: 0.75rem;
}

.section p {
    color: #333333;
    font-size: 1rem;
    line-height: 1.6;
}

@media (max-width: 768px) {
    .about-section {
        padding: 20px 10px;
    }

    .section {
        margin: 1rem 0;
        padding: 1rem;
    }

    main {
        padding: 20px 10px;
    }
}

@media (max-width: 480px) {
    .about-section {
        padding: 10px;
    }

    .hero h1 {
        font-size: 36px;
    }
}
</style>

