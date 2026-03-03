<template>
  <PageLayout>
    <HeroSection
      title="EV Charging Station"
      subtitle="Power up at our on-site fast-charging station in Kicukiro, Kigali — open to all EV owners"
      backgroundImage="/charging.jpg"
    />

    <main>
      <section class="charging-intro">
        <h2>Charge With Confidence</h2>
        <p>Our dedicated EV charging station is located right at the Triple Goats showroom in Kicukiro, Kigali. Whether you drive a BYD, Dongfeng, Tesla, or any other electric vehicle, you are welcome to charge here. We support multiple connector standards and offer both fast DC charging and standard AC charging to suit your needs.</p>
      </section>

      <section class="charging-features">
        <h2>Charging Options</h2>
        <div class="features-grid">
          <div class="feature-card">
            <i class="fas fa-bolt"></i>
            <h3>DC Fast Charging</h3>
            <p>Get up to 80% charge in as little as 30-45 minutes with our high-power DC chargers. Ideal for quick top-ups when you are on the go.</p>
            <div class="spec-tag">Up to 120 kW</div>
          </div>
          <div class="feature-card">
            <i class="fas fa-plug"></i>
            <h3>AC Standard Charging</h3>
            <p>Perfect for longer stays — plug in while you browse our showroom or enjoy a coffee. Full charge typically takes 4-6 hours depending on battery size.</p>
            <div class="spec-tag">Up to 22 kW</div>
          </div>
          <div class="feature-card">
            <i class="fas fa-charging-station"></i>
            <h3>Supported Connectors</h3>
            <p>Our station supports CCS2, CHAdeMO, and Type 2 connectors — covering the vast majority of electric vehicles available in Rwanda and across Africa.</p>
            <div class="spec-tag">CCS2 / CHAdeMO / Type 2</div>
          </div>
          <div class="feature-card">
            <i class="fas fa-clock"></i>
            <h3>Operating Hours</h3>
            <p>Our charging station is open during showroom hours. Drive in anytime during business hours — no appointment or membership required.</p>
            <div class="spec-tag">Mon-Sat: 8:00 AM - 6:00 PM</div>
          </div>
        </div>
      </section>

      <section class="charging-info">
        <h2>How It Works</h2>
        <div class="steps-grid">
          <div class="step">
            <div class="step-number">1</div>
            <h3>Drive In</h3>
            <p>Pull into any available charging bay at our Kicukiro showroom. No reservation needed.</p>
          </div>
          <div class="step">
            <div class="step-number">2</div>
            <h3>Plug In</h3>
            <p>Select the right connector for your vehicle and plug in. Our staff are happy to assist if needed.</p>
          </div>
          <div class="step">
            <div class="step-number">3</div>
            <h3>Charge Up</h3>
            <p>Relax in our showroom, browse our latest models, or take a stroll while your vehicle charges.</p>
          </div>
          <div class="step">
            <div class="step-number">4</div>
            <h3>Pay &amp; Go</h3>
            <p>Pay per kWh consumed. We accept mobile money, cash, and card payments. Then drive away fully charged.</p>
          </div>
        </div>
      </section>
    </main>

    <section class="map-section">
      <h2>Find Us</h2>
      <p class="map-hint">Our charging station is located at the Triple Goats showroom, Kicukiro, Kigali.</p>
      <div class="map-container">
        <iframe
          src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d1993.7091439229293!2d30.10151!3d-1.987428!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x19dcb909c976d39b%3A0x85b1db1ad0e495c5!2z5Y-B576K5rG96L2mIFRnIEVsZWN0cmluIENhciBNYXJrZXQ!5e0!3m2!1szh-CN!2srw!4v1738853579832!5m2!1szh-CN!2srw"
          width="100%"
          height="450"
          style="border:0;"
          allowfullscreen=""
          loading="lazy"
          referrerpolicy="no-referrer-when-downgrade">
        </iframe>
      </div>
    </section>
  </PageLayout>
</template>

<script setup>
import { useHead } from '@unhead/vue'
import PageLayout from '@/components/PageLayout.vue'
import HeroSection from '@/components/HeroSection.vue'

useHead({
  title: 'EV Charging Stations — Triple Goats Kigali',
  meta: [
    { name: 'description', content: 'Find EV charging stations in Kigali. Fast and reliable charging for all electric vehicle brands.' },
    { property: 'og:title', content: 'EV Charging Stations — Triple Goats Kigali' },
    { property: 'og:description', content: 'Find EV charging stations in Kigali. Fast and reliable charging for all electric vehicle brands.' },
    { property: 'og:url', content: 'https://tgautomobile.com/charging' },
  ],
  link: [
    { rel: 'canonical', href: 'https://tgautomobile.com/charging' }
  ]
})
</script>

<style scoped>
main {
  padding: 50px 20px;
  background: var(--primary-color);
}

section { margin-bottom: 3rem; }

h2 {
  font-size: 2rem; text-align: center; margin-bottom: 1rem; color: var(--secondary-color);
}

.charging-intro { max-width: 800px; margin: 0 auto 3rem; text-align: center; }
.charging-intro p { font-size: 1.1rem; line-height: 1.8; color: var(--text-color); }

.features-grid {
  display: grid; grid-template-columns: repeat(2, 1fr); gap: 1.5rem;
  max-width: 1000px; margin: 0 auto;
}

.feature-card {
  background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 1rem; padding: 2rem; text-align: center; transition: transform 0.3s, box-shadow 0.3s;
}
.feature-card:hover { transform: translateY(-4px); box-shadow: 0 8px 30px rgba(0, 0, 0, 0.3); }
.feature-card i { font-size: 2.5rem; color: var(--accent-color); margin-bottom: 1rem; }
.feature-card h3 { font-size: 1.25rem; margin-bottom: 0.75rem; color: var(--secondary-color); }
.feature-card p { font-size: 0.95rem; line-height: 1.6; color: var(--text-color); margin-bottom: 1rem; }
.spec-tag {
  display: inline-block; background: var(--accent-color); color: white;
  padding: 0.375rem 1rem; border-radius: 9999px; font-size: 0.85rem; font-weight: 600;
}

.steps-grid {
  display: grid; grid-template-columns: repeat(4, 1fr); gap: 1.5rem;
  max-width: 1000px; margin: 0 auto;
}

.step { text-align: center; }
.step-number {
  width: 48px; height: 48px; border-radius: 50%; background: var(--accent-color);
  color: white; display: flex; align-items: center; justify-content: center;
  font-size: 1.5rem; font-weight: 700; margin: 0 auto 1rem;
}
.step h3 { font-size: 1.1rem; margin-bottom: 0.5rem; color: var(--secondary-color); }
.step p { font-size: 0.9rem; line-height: 1.6; color: var(--text-color); }

.map-section {
  padding: 3rem 20px; background: var(--primary-color); text-align: center;
}
.map-hint { color: var(--text-color); margin-bottom: 1.5rem; }
.map-container { max-width: 1000px; margin: 0 auto; border-radius: 1rem; overflow: hidden; }

@media (max-width: 768px) {
  .features-grid { grid-template-columns: 1fr; }
  .steps-grid { grid-template-columns: repeat(2, 1fr); }
  h2 { font-size: 1.5rem; }
}

@media (max-width: 480px) {
  .steps-grid { grid-template-columns: 1fr; }
  main { padding: 30px 15px; }
}
</style>

