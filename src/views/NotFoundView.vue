<template>
  <PageLayout>

    <main>
      <div class="container">
        <div class="error-icon">
          <i class="fas fa-exclamation-triangle"></i>
        </div>
        <h1>404</h1>
        <h2>Page Not Found</h2>
        <p>Sorry, the page you are looking for does not exist or has been moved.</p>
        <div class="actions">
          <router-link to="/home" class="btn btn-primary">Back to Home</router-link>
          <router-link to="/inventory" class="btn btn-outline">Browse Inventory</router-link>
        </div>
      </div>
    </main>
  </PageLayout>
</template>

<script setup>
import { useHead } from '@unhead/vue'
import PageLayout from '@/components/PageLayout.vue'

useHead({
  title: 'Page Not Found — Triple Goats',
  meta: [
    { name: 'description', content: 'The page you are looking for does not exist.' },
    { name: 'robots', content: 'noindex' }
  ]
})
</script>

<style scoped>
main {
    padding: 100px 20px;
    background: var(--primary-color);
    text-align: center;
    min-height: 60vh;
    display: flex;
    align-items: center;
    justify-content: center;
}

.container {
    max-width: 600px;
}

.error-icon {
    font-size: 4rem;
    color: var(--accent-color);
    margin-bottom: 1.5rem;
}

h1 {
    font-size: 6rem;
    font-weight: 700;
    color: var(--secondary-color);
    line-height: 1;
    margin-bottom: 0.5rem;
}

h2 {
    font-size: 1.8rem;
    color: var(--text-color);
    margin-bottom: 1rem;
}

p {
    font-size: 1.1rem;
    color: var(--text-muted);
    margin-bottom: 2.5rem;
}

.actions {
    display: flex;
    justify-content: center;
    gap: 1.5rem;
    flex-wrap: wrap;
}

.btn-primary {
    background-color: var(--accent-color);
    color: white;
}

.btn-outline {
    border: 2px solid rgba(255, 255, 255, 0.2);
    color: white;
    background: transparent;
}

.btn-outline:hover {
    border-color: white;
    background: white;
    color: var(--primary-color);
}

@media (max-width: 768px) {
    h1 {
        font-size: 4rem;
    }

    h2 {
        font-size: 1.4rem;
    }

    main {
        padding: 60px 20px;
    }
}
</style>

