<template>
  <PageLayout>
    <HeroSection
      title="SUV Collection"
      subtitle="Command the road with confidence — explore our lineup of electric SUVs built for African terrain"
      backgroundImage="/images/pages/suv.jpg"
    />

    <main>
      <h2>SUV Models</h2>
      <p>Our electric SUVs combine bold design, generous ground clearance, and advanced all-wheel-drive systems to handle everything from Kigali's urban streets to Rwanda's rolling hills. With spacious interiors, panoramic views, and cutting-edge safety features, these vehicles are built for families, businesses, and anyone who refuses to compromise between capability and sustainability. Browse our current SUV inventory below.</p>
      <router-link to="/inventory?type=suv" class="btn">Explore SUV Inventory</router-link>
    </main>
  </PageLayout>
</template>

<script setup>
import { useHead } from '@unhead/vue'
import PageLayout from '@/components/PageLayout.vue'
import HeroSection from '@/components/HeroSection.vue'

useHead({
  title: 'Electric SUV Collection — Triple Goats',
  meta: [
    { name: 'description', content: 'Explore our lineup of electric SUVs built for African terrain. Bold design, generous ground clearance, and advanced safety features.' },
    { property: 'og:title', content: 'Electric SUV Collection — Triple Goats' },
    { property: 'og:description', content: 'Explore our lineup of electric SUVs built for African terrain. Bold design, generous ground clearance, and advanced safety features.' },
    { property: 'og:url', content: 'https://tgautomobile.com/suv' },
  ],
  link: [
    { rel: 'canonical', href: 'https://tgautomobile.com/suv' }
  ]
})
</script>

<style scoped>
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

