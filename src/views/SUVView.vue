<template>
  <div class="suv-page">
    <HeaderNav />
    
    <div class="hero">
      <h1>SUV Collection</h1>
      <p>Command the road with confidence — explore our lineup of electric SUVs built for African terrain</p>
    </div>

    <main>
      <h2>SUV Models</h2>
      <p>Our electric SUVs combine bold design, generous ground clearance, and advanced all-wheel-drive systems to handle everything from Kigali's urban streets to Rwanda's rolling hills. With spacious interiors, panoramic views, and cutting-edge safety features, these vehicles are built for families, businesses, and anyone who refuses to compromise between capability and sustainability. Browse our current SUV inventory below.</p>
      <router-link to="/inventory?type=suv" class="btn">Explore SUV Inventory</router-link>
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
    background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('/suv.jpg');
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
    margin-bottom: 30px;
}
</style>

