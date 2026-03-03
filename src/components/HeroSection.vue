<template>
  <div class="hero" :class="heroClass" :style="heroStyle">
    <!-- 视频背景模式 -->
    <template v-if="backgroundVideo">
      <video autoplay muted loop playsinline class="hero-video">
        <source :src="backgroundVideo" type="video/mp4">
      </video>
      <div class="hero-overlay"></div>
    </template>

    <div class="hero-content">
      <h1>{{ title }}</h1>
      <p v-if="subtitle">{{ subtitle }}</p>
      <slot></slot>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  title: {
    type: String,
    required: true
  },
  subtitle: {
    type: String,
    default: ''
  },
  backgroundImage: {
    type: String,
    default: ''
  },
  backgroundVideo: {
    type: String,
    default: ''
  },
  height: {
    type: String,
    default: ''
  }
})

const heroClass = computed(() => ({
  'hero--image': !!props.backgroundImage && !props.backgroundVideo,
  'hero--video': !!props.backgroundVideo,
  'hero--gradient': !props.backgroundImage && !props.backgroundVideo
}))

const heroStyle = computed(() => {
  const style = {}
  if (props.backgroundImage && !props.backgroundVideo) {
    style.backgroundImage = `linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('${props.backgroundImage}')`
  }
  if (props.height) {
    style.height = props.height
  }
  return style
})
</script>

<style scoped>
/* 基础 Hero 样式 */
.hero {
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    color: var(--secondary-color);
    text-align: center;
    overflow: hidden;
}

/* 纯渐变背景模式 */
.hero--gradient {
    background: linear-gradient(135deg, #1e3a5f 0%, #0f172a 50%, #1a1a2e 100%);
    padding: 60px 20px;
}

/* 图片背景模式 */
.hero--image {
    height: 60vh;
    background-size: cover;
    background-position: center;
}

/* 视频背景模式 */
.hero--video {
    height: 60vh;
}

.hero-video {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
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
    max-width: 900px;
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
}

@media (max-width: 768px) {
    .hero--image,
    .hero--video {
        height: 40vh;
    }

    .hero h1 {
        font-size: 28px;
    }

    .hero p {
        font-size: 16px;
    }
}
</style>

