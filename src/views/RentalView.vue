<template>
  <PageLayout>
    <HeroSection
      title="Car Rental Services"
      subtitle="Drive electric on your own schedule — short-term and long-term rentals available in Kigali"
      backgroundImage="/rental.png"
    />

    <main>
      <section class="rental-intro">
        <div class="coming-soon-badge"><i class="fas fa-tools"></i> Coming Soon</div>
        <h2>Electric Car Rental Program</h2>
        <p>We are putting the finishing touches on our electric car rental program. Soon you will be able to rent a fully charged EV for a day trip to Nyungwe, a week-long business engagement, or anything in between. Our rental fleet will include compact sedans, spacious SUVs, and versatile vans — all maintained to showroom standards.</p>
      </section>

      <section class="rental-features">
        <h2>What to Expect</h2>
        <div class="features-grid">
          <div class="feature-card">
            <i class="fas fa-car"></i>
            <h3>Diverse Fleet</h3>
            <p>Choose from a range of electric models — compact city cars for urban errands, midsize sedans for business trips, or spacious SUVs for family adventures across Rwanda.</p>
          </div>
          <div class="feature-card">
            <i class="fas fa-battery-full"></i>
            <h3>Fully Charged</h3>
            <p>Every rental vehicle is delivered to you with a full battery. We also provide information on charging stations across Kigali and beyond so you never run low.</p>
          </div>
          <div class="feature-card">
            <i class="fas fa-calendar-alt"></i>
            <h3>Flexible Duration</h3>
            <p>Rent by the day, week, or month. Whether you need a car for a quick airport transfer or a three-month project, we have competitive rates for every duration.</p>
          </div>
          <div class="feature-card">
            <i class="fas fa-shield-alt"></i>
            <h3>Full Coverage</h3>
            <p>All rentals include comprehensive insurance, roadside assistance, and 24/7 support. Drive with confidence knowing you are fully protected.</p>
          </div>
        </div>
      </section>

      <section class="rental-cta">
        <h2>Interested? Get in Touch</h2>
        <p>While our online booking system is under development, you can contact us directly to arrange a rental. We will do our best to accommodate your needs right away.</p>
        <div class="cta-buttons">
          <router-link to="/contact" class="btn btn-primary">Contact Us</router-link>
          <router-link to="/inventory" class="btn btn-outline">Browse Our Vehicles</router-link>
        </div>
      </section>
    </main>
  </PageLayout>
</template>

<script setup>
import { useHead } from '@unhead/vue'
import PageLayout from '@/components/PageLayout.vue'
import HeroSection from '@/components/HeroSection.vue'

useHead({
  title: 'Electric Car Rental — Triple Goats Kigali',
  meta: [
    { name: 'description', content: 'Rent a fully charged EV for a day trip, business engagement, or anything in between. Short-term and long-term rentals available.' },
    { property: 'og:title', content: 'Electric Car Rental — Triple Goats Kigali' },
    { property: 'og:description', content: 'Rent a fully charged EV for a day trip, business engagement, or anything in between. Short-term and long-term rentals available.' },
    { property: 'og:url', content: 'https://tgautomobile.com/rental' },
  ],
  link: [
    { rel: 'canonical', href: 'https://tgautomobile.com/rental' }
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

.coming-soon-badge {
  display: inline-block; background: var(--accent-color); color: white;
  padding: 0.5rem 1.5rem; border-radius: 9999px; font-weight: 600;
  font-size: 0.9rem; margin-bottom: 1.5rem;
}

.rental-intro { max-width: 800px; margin: 0 auto 3rem; text-align: center; }
.rental-intro p { font-size: 1.1rem; line-height: 1.8; color: var(--text-color); }

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
.feature-card p { font-size: 0.95rem; line-height: 1.6; color: var(--text-color); }

.rental-cta { text-align: center; max-width: 700px; margin: 0 auto; }
.rental-cta p { font-size: 1.1rem; color: var(--text-color); line-height: 1.8; margin-bottom: 2rem; }

.cta-buttons { display: flex; justify-content: center; gap: 1.5rem; flex-wrap: wrap; }
.btn {
  display: inline-block; padding: 0.875rem 2rem; border-radius: 9999px;
  text-decoration: none; font-weight: 600; font-size: 1rem; transition: all 0.3s;
}
.btn-primary { background: var(--accent-color); color: white; }
.btn-primary:hover { background: var(--accent-color-dark); transform: translateY(-2px); }
.btn-outline {
  border: 2px solid rgba(255, 255, 255, 0.3); color: white; background: transparent;
}
.btn-outline:hover { border-color: white; background: white; color: var(--primary-color); }

@media (max-width: 768px) {
  .features-grid { grid-template-columns: 1fr; }
  h2 { font-size: 1.5rem; }
}

@media (max-width: 480px) {
  main { padding: 30px 15px; }
  .cta-buttons { flex-direction: column; align-items: center; }
}
</style>

