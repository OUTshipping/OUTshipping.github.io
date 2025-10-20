<template>
  <div class="contact-page">
    <HeaderNav />
    
    <div class="hero">
      <h1>Get in Touch</h1>
      <p>We are here to help you with any questions or concerns</p>
    </div>

    <div class="info-cards">
      <div class="card">
        <div class="card-content">
          <div class="card-icon">
            <img src="/phone-icon.png" alt="Phone Icon" class="card-icon">
          </div>
          <div class="card-details">
            <h3>Contact</h3>
            <p>
              <a href="https://wa.me/250785084313" target="_blank">Phone: +250 785 084 313</a> /
              <a href="https://wa.me/250794104908" target="_blank">+250 794 104 908</a>
            </p>
            <p>Email: tgautomobile@gmail.com</p>
          </div>
        </div>
      </div>
      <div class="card">
        <div class="card-content">
          <div class="card-icon">
            <img src="/location-icon.png" alt="Location Icon" class="card-icon">
          </div>
          <div class="card-details">
            <h3>Location</h3>
            <p>Address: KK 15 Rd, Kicukiro, Kigali</p>
            <p>City: Kigali</p>
            <p>Country: Rwanda</p>
          </div>
        </div>
      </div>
      <div class="card">
        <div class="card-content">
          <div class="card-icon">
            <img src="/time-icon.png" alt="Time Icon" class="card-icon">
          </div>
          <div class="card-details">
            <h3>Business Hours</h3>
            <p>Monday - Friday: 9:00 AM - 6:00 PM UTC+2</p>
            <p>Weekend: Closed</p>
          </div>
        </div>
      </div>
    </div>

    <main>
      <div class="form-container">
        <div class="embedded-form">
          <iframe 
            src="https://docs.google.com/forms/d/e/1FAIpQLSdGsQemQKBRHJn9ODs3DbSn4E9PFRtMUwcW2boTwIPgcnfJQA/viewform?embedded=true" 
            width="100%" 
            height="600" 
            frameborder="0" 
            marginheight="0" 
            marginwidth="0">
            Your browser does not support iframes.
          </iframe>
        </div>
      </div>

      <div class="map-container">
        <div id="map">
          <iframe 
            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d15949.673151412455!2d30.08305617980293!3d-1.9874279969959143!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x19dcb909c976d39b%3A0x85b1db1ad0e495c5!2z5Y-B576K5rG96L2mIFRnIEVsZWN0cmljIENhciBNYXJrZXQ!5e0!3m2!1szh-CN!2srw!4v1739439963365!5m2!1szh-CN!2srw" 
            width="100%" 
            height="100%" 
            style="border:0;" 
            allowfullscreen="" 
            loading="lazy" 
            referrerpolicy="no-referrer-when-downgrade">
          </iframe>
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
    background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('/contact.png');
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

.info-cards {
    display: flex;
    gap: 20px;
    justify-content: center;
    padding: 40px 20px;
    background: var(--primary-color);
}

.card {
    background: var(--secondary-color);
    color: var(--primary-color);
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    flex: 1;
    max-width: 100%;
    box-shadow: 0 6px 15px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s;
}

.card:hover {
    transform: scale(1.05);
}

.card-content {
    display: flex;
    align-items: flex-start;
    gap: 15px;
    padding: 10px 0;
}

.card-icon {
    width: 60px;
    height: 60px;
    background-color: var(--accent-color);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--primary-color);
    font-size: 24px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

.card-icon img {
    max-width: 80%;
    max-height: 80%;
}

.card-details {
    flex: 1;
    text-align: left;
}

.card-details h3 {
    font-size: 24px;
    margin: 0;
    color: var(--accent-color);
    text-transform: uppercase;
    font-weight: bold;
}

.card-details p {
    font-size: 16px;
    line-height: 1.5;
    margin: 5px;
}

main {
    padding: 50px 20px;
    background: var(--primary-color);
    display: flex;
    gap: 40px;
    flex-wrap: wrap;
}

.form-container,
.map-container {
    flex: 1;
    background: var(--secondary-color);
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
}

#map {
    width: 100%;
    height: 100%;
}

.embedded-form {
    width: 100%;
    height: 600px;
}

@media (max-width: 768px) {
    .info-cards {
        flex-direction: column;
    }

    .card {
        padding: 20px;
        border-radius: 15px;
    }

    main {
        flex-direction: column;
    }

    .form-container,
    .map-container {
        padding: 20px;
    }
}
</style>

