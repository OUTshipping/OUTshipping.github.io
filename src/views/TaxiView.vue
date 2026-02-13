<template>
  <div class="taxi-page">
    <HeaderNav />
    
    <div class="hero">
      <h1>Taxi Service</h1>
      <p>Clean, quiet, and affordable electric taxi rides across Kigali</p>
    </div>

    <main>
      <h2>Coming Soon</h2>
      <p>We are building a fleet of fully electric taxis to serve Kigali and beyond. Expect professional drivers, air-conditioned cabins, real-time ride tracking, and cashless payment — all powered by zero-emission vehicles. Whether you need a daily commute, an airport transfer, or a ride across town, our EV taxi service will offer a greener, more comfortable alternative. Stay tuned for our official launch, or reach out to us now if you would like to be notified when bookings open.</p>
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
    background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('/taxi.png');
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
    font-size: 36px;
    margin-bottom: 20px;
}

main p {
    font-size: 18px;
}
</style>

