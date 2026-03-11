<template>
  <PageLayout>
    <HeroSection
      title="Get in Touch"
      subtitle="Have a question about a vehicle, need a quote, or want to schedule a visit? Our teams in Kigali and Gisenyi are here to help — reach out anytime."
      backgroundImage="/images/pages/contact.jpg"
    />

    <div class="info-cards">
      <div class="card">
        <div class="card-content">
          <div class="card-icon">
            <img src="/images/icons/phone-icon.png" alt="Phone Icon" class="card-icon">
          </div>
          <div class="card-details">
            <h3>Contact</h3>
            <p>
              <a href="https://wa.me/250785084313" target="_blank">Phone: +250 785 084 313</a> /
              <a href="https://wa.me/250794104908" target="_blank">+250 794 104 908</a>
            </p>
            <p>Email: tgautomobile@gmail.com</p>
            <p>WhatsApp available — tap the numbers above to chat directly with our sales team.</p>
          </div>
        </div>
      </div>
      <div class="card">
        <div class="card-content">
          <div class="card-icon">
            <img src="/images/icons/location-icon.png" alt="Location Icon" class="card-icon">
          </div>
          <div class="card-details">
            <h3>Locations</h3>
            <p><strong>Kigali:</strong> KK 15 Rd, Kicukiro, Kigali</p>
            <p><strong>Gisenyi:</strong> 8754+JCC, Rubavu</p>
            <p>Two showrooms across Rwanda — visit the one nearest to you. Look for the Triple Goats signage and our outdoor EV display.</p>
          </div>
        </div>
      </div>
      <div class="card">
        <div class="card-content">
          <div class="card-icon">
            <img src="/images/icons/time-icon.png" alt="Time Icon" class="card-icon">
          </div>
          <div class="card-details">
            <h3>Business Hours</h3>
            <p>Monday - Friday: 9:00 AM - 6:00 PM (CAT, UTC+2)</p>
            <p>Saturday: 9:00 AM - 1:00 PM</p>
            <p>Sunday: Closed</p>
            <p>Walk-ins welcome during business hours. For after-hours inquiries, leave us a WhatsApp message and we will respond first thing next morning.</p>
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
            marginwidth="0"
            title="Contact Form">
            Your browser does not support iframes.
          </iframe>
        </div>
      </div>

      <div class="map-grid">
        <div class="map-container">
          <h3 class="map-label">Kigali Showroom</h3>
          <div id="map-kigali">
            <iframe
              src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d15949.673151412455!2d30.08305617980293!3d-1.9874279969959143!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x19dcb909c976d39b%3A0x85b1db1ad0e495c5!2z5Y-B576K5rG96L2mIFRnIEVsZWN0cmljIENhciBNYXJrZXQ!5e0!3m2!1szh-CN!2srw!4v1739439963365!5m2!1szh-CN!2srw"
              width="100%"
              height="100%"
              style="border:0;"
              allowfullscreen=""
              loading="lazy"
              referrerpolicy="no-referrer-when-downgrade"
              title="Triple Goats Kigali Showroom Location">
            </iframe>
          </div>
        </div>
        <div class="map-container">
          <h3 class="map-label">Gisenyi Showroom</h3>
          <div id="map-gisenyi">
            <iframe
              src="https://www.google.com/maps?q=8754%2BJCC+Rubavu+Rwanda&output=embed"
              width="100%"
              height="100%"
              style="border:0;"
              allowfullscreen=""
              loading="lazy"
              referrerpolicy="no-referrer-when-downgrade"
              title="Triple Goats Gisenyi Showroom Location">
            </iframe>
          </div>
        </div>
      </div>
    </main>

  </PageLayout>
</template>

<script setup>
import { useHead } from '@unhead/vue'
import PageLayout from '@/components/PageLayout.vue'
import HeroSection from '@/components/HeroSection.vue'

useHead({
  title: 'Contact Us — Triple Goats Kigali & Gisenyi Showrooms',
  meta: [
    { name: 'description', content: 'Visit our showrooms in Kigali and Gisenyi, call us, or send a WhatsApp message. Open Monday–Friday 9am–6pm, Saturday 9am–1pm.' },
    { property: 'og:title', content: 'Contact Us — Triple Goats Kigali & Gisenyi Showrooms' },
    { property: 'og:description', content: 'Visit our showrooms in Kigali and Gisenyi, call us, or send a WhatsApp message. Open Monday–Friday 9am–6pm, Saturday 9am–1pm.' },
    { property: 'og:url', content: 'https://tgautomobile.com/contact' },
    { property: 'og:image', content: 'https://tgautomobile.com/images/pages/contact.jpg' },
  ],
  link: [
    { rel: 'canonical', href: 'https://tgautomobile.com/contact' }
  ]
})
</script>

<style scoped>
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
    flex-direction: column;
    gap: 40px;
}

.form-container {
    background: var(--secondary-color);
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
}

.map-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
}

.map-container {
    background: var(--secondary-color);
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
}

.map-label {
    font-size: 1.1rem;
    font-weight: 600;
    color: var(--accent-color);
    margin-bottom: 12px;
    text-align: center;
}

#map-kigali,
#map-gisenyi {
    width: 100%;
    height: 350px;
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

    .map-grid {
        grid-template-columns: 1fr;
    }

    .form-container,
    .map-container {
        padding: 20px;
    }
}
</style>

