<template>
  <PageLayout>
    
    <div class="hero">
      <video autoplay muted loop playsinline class="hero-video">
        <source src="/video/taxi.mp4" type="video/mp4">
      </video>
      <div class="hero-overlay"></div>
      <div class="hero-content">
        <h1>Taxi Service</h1>
        <p>Clean, quiet, and affordable electric taxi rides across Kigali</p>
      </div>
    </div>

    <main>
      <section class="taxi-intro">
        <div class="intro-image">
          <img src="/images/pages/taxi.jpg" alt="Triple Goats Electric Taxi" loading="lazy">
        </div>
        <div class="intro-text">
          <h2>Your Ride, Electrified</h2>
          <p>Our fleet of fully electric taxis is now serving Kigali and beyond. Enjoy professional drivers, air-conditioned cabins, real-time ride tracking, and cashless payment — all powered by zero-emission vehicles.</p>
          <p>Whether you need a daily commute, an airport transfer, or a ride across town, our EV taxi service offers a greener, more comfortable alternative to traditional transport.</p>
        </div>
      </section>

      <section class="taxi-features">
        <h2>Why Choose Our Electric Taxi?</h2>
        <div class="features-grid">
          <div class="feature-item">
            <i class="fas fa-leaf"></i>
            <h3>Zero Emissions</h3>
            <p>Every ride is 100% electric — no exhaust, no noise pollution, just a clean journey through the city.</p>
          </div>
          <div class="feature-item">
            <i class="fas fa-shield-alt"></i>
            <h3>Safe &amp; Professional</h3>
            <p>Licensed, trained drivers and well-maintained vehicles with modern safety features for your peace of mind.</p>
          </div>
          <div class="feature-item">
            <i class="fas fa-money-bill-wave"></i>
            <h3>Affordable Rates</h3>
            <p>Competitive pricing with transparent fares. No hidden charges — what you see is what you pay.</p>
          </div>
          <div class="feature-item">
            <i class="fas fa-snowflake"></i>
            <h3>Air-Conditioned Comfort</h3>
            <p>Enjoy a cool, comfortable ride every time — even on the hottest Kigali afternoons.</p>
          </div>
        </div>
      </section>


    </main>
  </PageLayout>
</template>

<script setup>
import { useHead } from '@unhead/vue'
import PageLayout from '@/components/PageLayout.vue'

useHead({
  title: 'Electric Taxi Service — Triple Goats Kigali',
  meta: [
    { name: 'description', content: 'Clean, quiet, and affordable electric taxi rides across Kigali. Professional drivers, air-conditioned cabins, zero emissions.' },
    { property: 'og:title', content: 'Electric Taxi Service — Triple Goats Kigali' },
    { property: 'og:description', content: 'Clean, quiet, and affordable electric taxi rides across Kigali. Professional drivers, air-conditioned cabins, zero emissions.' },
    { property: 'og:url', content: 'https://tgautomobile.com/taxi' },
  ],
  link: [
    { rel: 'canonical', href: 'https://tgautomobile.com/taxi' }
  ]
})
</script>

<style scoped>
/* Hero with video background */
.hero {
    position: relative;
    height: 70vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    color: var(--secondary-color);
    text-align: center;
    overflow: hidden;
}

.hero-video {
    position: absolute;
    top: 50%;
    left: 50%;
    min-width: 100%;
    min-height: 100%;
    transform: translate(-50%, -50%);
    object-fit: cover;
    z-index: 0;
}

.hero-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    z-index: 1;
}

.hero-content {
    position: relative;
    z-index: 2;
    max-width: 800px;
    padding: 0 20px;
}

.hero h1 {
    font-size: 48px;
    margin-bottom: 20px;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
}

.hero p {
    font-size: 24px;
    margin-bottom: 30px;
    text-shadow: 0 1px 3px rgba(0, 0, 0, 0.4);
}

/* Intro section */
.taxi-intro {
    display: flex;
    gap: 40px;
    align-items: center;
    max-width: 1100px;
    margin: 0 auto;
    padding: 60px 20px;
}

.intro-image {
    flex: 1;
    border-radius: 15px;
    overflow: hidden;
    box-shadow: var(--shadow-lg);
}

.intro-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
}

.intro-text {
    flex: 1;
}

.intro-text h2 {
    font-size: 32px;
    margin-bottom: 20px;
    color: var(--secondary-color);
}

.intro-text p {
    font-size: 17px;
    line-height: 1.7;
    color: var(--text-muted);
    margin-bottom: 15px;
}

/* Features grid */
.taxi-features {
    max-width: 1100px;
    margin: 0 auto;
    padding: 60px 20px;
    text-align: center;
}

.taxi-features h2 {
    font-size: 32px;
    margin-bottom: 40px;
    color: var(--secondary-color);
}

.features-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 30px;
}

.feature-item {
    background: rgba(255, 255, 255, 0.05);
    border-radius: 15px;
    padding: 30px 20px;
    transition: transform 0.3s, box-shadow 0.3s;
}

.feature-item:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.2);
}

.feature-item i {
    font-size: 36px;
    color: var(--accent-color);
    margin-bottom: 15px;
}

.feature-item h3 {
    font-size: 20px;
    margin-bottom: 10px;
    color: var(--secondary-color);
}

.feature-item p {
    font-size: 15px;
    line-height: 1.6;
    color: var(--text-muted);
}



main {
    background: var(--primary-color);
}

@media (max-width: 768px) {
    .hero {
        height: 50vh;
    }

    .hero h1 {
        font-size: 32px;
    }

    .hero p {
        font-size: 18px;
    }

    .taxi-intro {
        flex-direction: column;
        padding: 40px 15px;
    }

    .taxi-features {
        padding: 40px 15px;
    }

}
</style>

