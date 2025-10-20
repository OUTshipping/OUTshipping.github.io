<template>
  <div class="testdrive-page">
    <HeaderNav />
    
    <div class="hero">
      <h1>Schedule a Test Drive</h1>
      <p>Experience our vehicles firsthand</p>
    </div>

    <main>
      <div class="form-container">
        <iframe 
          src="https://docs.google.com/forms/d/e/1FAIpQLSdGsQemQKBRHJn9ODs3DbSn4E9PFRtMUwcW2boTwIPgcnfJQA/viewform?embedded=true" 
          width="100%" 
          height="800" 
          frameborder="0" 
          marginheight="0" 
          marginwidth="0">
          Your browser does not support iframes.
        </iframe>
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
    background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('/testdrive.png');
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
}

.form-container {
    max-width: 1000px;
    margin: 0 auto;
    background: var(--secondary-color);
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
}
</style>

