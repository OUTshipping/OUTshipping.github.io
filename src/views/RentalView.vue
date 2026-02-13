<template>
  <div class="rental-page">
    <HeaderNav />
    
    <div class="hero">
      <h1>Car Rental Services</h1>
      <p>Drive electric on your own schedule — short-term and long-term rentals available in Kigali</p>
    </div>

    <main>
      <h2>Coming Soon</h2>
      <p>We are putting the finishing touches on our electric car rental program. Soon you will be able to rent a fully charged EV for a day trip to Nyungwe, a week-long business engagement, or anything in between. Our rental fleet will include compact sedans, spacious SUVs, and versatile vans — all maintained to showroom standards. In the meantime, feel free to contact us directly if you have an immediate rental need and we will do our best to accommodate you.</p>
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
    background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('/rental.png');
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

