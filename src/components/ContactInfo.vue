<template>
  <section class="cta-section">
    <div class="container">
        <div class="cta-content">
            <h2>Ready to Electrify Your Journey?</h2>
            <p>Join the green revolution today with Triple Goats. Schedule a test drive or visit our showroom.</p>
            <div class="cta-actions">
                <router-link to="/testdrive" class="btn btn-primary">Schedule Test Drive</router-link>
                <router-link to="/contact" class="btn btn-outline">Contact Sales</router-link>
            </div>
        </div>
    </div>
  </section>
</template>

<script setup>
// Contact Info / CTA Component
</script>

<style scoped>
.cta-section {
    padding: 5rem 0;
    background: linear-gradient(135deg, var(--primary-color), var(--card-bg-color));
    color: white;
    text-align: center;
    position: relative;
    overflow: hidden;
}

.cta-section::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: url('/pattern.png') repeat; /* Optional pattern */
    opacity: 0.05;
}

.cta-content {
    position: relative;
    z-index: 1;
    max-width: 700px;
    margin: 0 auto;
}

h2 {
    font-size: 2.5rem;
    margin-bottom: 1.5rem;
    font-weight: 700;
}

p {
    font-size: 1.1rem;
    margin-bottom: 2.5rem;
    color: var(--text-muted);
}

.cta-actions {
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
    .cta-section {
        padding: 4rem 1rem;
    }

    h2 {
        font-size: 2rem;
    }
}
</style>

