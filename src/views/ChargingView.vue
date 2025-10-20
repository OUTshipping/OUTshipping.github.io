<template>
  <div class="charging-page">
    <HeaderNav />
    
    <div class="map-container">
      <iframe 
        src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d1993.7091439229293!2d30.10151!3d-1.987428!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x19dcb909c976d39b%3A0x85b1db1ad0e495c5!2z5Y-B576K5rG96L2mIFRnIEVsZWN0cmluIENhciBNYXJrZXQ!5e0!3m2!1szh-CN!2srw!4v1738853579832!5m2!1szh-CN!2srw" 
        width="100%" 
        height="600px" 
        style="border:0;" 
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
.map-container {
    padding: 20px 0;
    background-color: #f5f5f5;
}
</style>

