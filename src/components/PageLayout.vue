<template>
  <div class="page-layout">
    <HeaderNav />

    <slot></slot>

    <ContactInfo v-if="showContactInfo" />
    <SocialMedia v-if="showSocialMedia" />
    <FooterBar v-if="showFooter" />

    <!-- WhatsApp 浮动按钮 -->
    <div class="whatsapp-widget">
      <div class="whatsapp-menu" v-if="waMenuOpen">
        <a href="https://wa.me/250785084313" target="_blank" rel="noopener" class="wa-item">
          <i class="fab fa-whatsapp"></i>
          <span>+250 785 084 313</span>
        </a>
        <a href="https://wa.me/250794104908" target="_blank" rel="noopener" class="wa-item">
          <i class="fab fa-whatsapp"></i>
          <span>+250 794 104 908</span>
        </a>
      </div>
      <button class="whatsapp-fab" @click="waMenuOpen = !waMenuOpen" aria-label="Chat on WhatsApp">
        <i :class="waMenuOpen ? 'fas fa-times' : 'fab fa-whatsapp'"></i>
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import HeaderNav from '@/components/HeaderNav.vue'
import FooterBar from '@/components/FooterBar.vue'
import SocialMedia from '@/components/SocialMedia.vue'
import ContactInfo from '@/components/ContactInfo.vue'

defineProps({
  showContactInfo: {
    type: Boolean,
    default: true
  },
  showSocialMedia: {
    type: Boolean,
    default: true
  },
  showFooter: {
    type: Boolean,
    default: true
  }
})

const waMenuOpen = ref(false)
</script>

<style scoped>
.whatsapp-widget {
  position: fixed;
  bottom: 28px;
  right: 28px;
  z-index: 999;
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 12px;
}

.whatsapp-menu {
  display: flex;
  flex-direction: column;
  gap: 8px;
  animation: waSlideUp 0.25s ease-out;
}

.wa-item {
  display: flex;
  align-items: center;
  gap: 10px;
  background: #25d366;
  color: white;
  text-decoration: none;
  padding: 10px 18px;
  border-radius: 28px;
  font-size: 0.9rem;
  font-weight: 600;
  white-space: nowrap;
  box-shadow: 0 3px 10px rgba(0, 0, 0, 0.25);
  transition: transform 0.2s, box-shadow 0.2s;
}

.wa-item i {
  font-size: 1.2rem;
}

.wa-item:hover {
  transform: scale(1.05);
  box-shadow: 0 4px 16px rgba(37, 211, 102, 0.5);
}

.whatsapp-fab {
  width: 60px;
  height: 60px;
  background: #25d366;
  border-radius: 50%;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 32px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
  transition: transform 0.2s, box-shadow 0.2s;
}

.whatsapp-fab:hover {
  transform: scale(1.1);
  box-shadow: 0 6px 20px rgba(37, 211, 102, 0.5);
}

@keyframes waSlideUp {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

@media (max-width: 768px) {
  .whatsapp-widget {
    bottom: 20px;
    right: 20px;
  }

  .whatsapp-fab {
    width: 52px;
    height: 52px;
    font-size: 28px;
  }

  .wa-item {
    padding: 9px 14px;
    font-size: 0.85rem;
  }
}
</style>

