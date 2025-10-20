<template>
  <div class="bottom-social-media">
    <a href="https://www.instagram.com/tg_auto_rwanda/" class="social-item" target="_blank" rel="noopener">
      <img src="/ins.jpg" alt="Instagram" loading="lazy">
    </a>
    <a href="https://x.com/Triple_Goats" class="social-item" target="_blank" rel="noopener">
      <img src="/X.jpg" alt="Twitter" loading="lazy">
    </a>
    <a href="https://www.facebook.com/TripleGoats" class="social-item" target="_blank" rel="noopener">
      <img src="/facebook.jpg" alt="Facebook" loading="lazy">
    </a>
    <a href="https://www.tiktok.com/@tg.auto.rwanda" class="social-item" target="_blank" rel="noopener">
      <img src="/tiktok.jpg" alt="TikTok" loading="lazy">
    </a>
  </div>
</template>

<script setup>
// 社交媒体组件
</script>

<style scoped>
.bottom-social-media {
    display: flex;
    justify-content: center;
    gap: 15px;
    padding: 20px 0;
    background: var(--primary-color);
}

.social-item img {
    width: 30px;
    height: 30px;
    object-fit: cover;
    transition: transform 0.3s, filter 0.3s;
}

.social-item img:hover {
    transform: scale(1.1) rotate(20deg);
    filter: brightness(1.2);
}

.social-item img:active {
    transform: scale(0.9) rotate(-15deg);
}
</style>

