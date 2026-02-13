<template>
  <header>
    <router-link to="/home" class="logo">
      <img src="/companylogo.jpg" alt="Triple Goats Logo" loading="lazy">
      <div class="logo-text">
        <h1>Triple Goats</h1>
        <p class="slogan">GREEN ENERGY GREEN LIFE</p>
      </div>
    </router-link>

    <!-- 移动端汉堡菜单按钮 -->
    <div class="menu-toggle" :class="{ active: menuOpen }" @click="toggleMenu" aria-label="Toggle Menu">
      <span></span>
      <span></span>
      <span></span>
    </div>

    <!-- 主导航 -->
    <nav id="nav-menu" :class="{ active: menuOpen }">
      <router-link to="/inventory" @click="closeMenu">INVENTORY</router-link>
      <router-link to="/charging" @click="closeMenu">CHARGING</router-link>
      <router-link to="/services" @click="closeMenu">SERVICES</router-link>

      <div class="dropdown" :class="{ active: dropdownOpen }">
        <div class="dropbtn" @click.stop="toggleDropdown">
            DISCOVER
            <i class="fas fa-chevron-down" style="font-size: 0.8em; margin-left: 4px;"></i>
        </div>
        <div class="dropdown-content">
          <router-link to="/testdrive" @click="closeMenu">TEST DRIVE</router-link>
          <router-link to="/taxi" @click="closeMenu">TAXI SERVICE</router-link>
          <router-link to="/rental" @click="closeMenu">CAR RENTAL</router-link>
          <router-link to="/about" @click="closeMenu">ABOUT</router-link>
          <router-link to="/contact" @click="closeMenu">CONTACT</router-link>
        </div>
      </div>

      <!-- 移动端社媒图标 -->
      <div class="top-social-media mobile-only" v-if="menuOpen">
          <a href="https://www.instagram.com/tg_auto_rwanda/" class="social-icon-link" target="_blank" rel="noopener" aria-label="Instagram">
            <i class="fab fa-instagram"></i>
          </a>
          <a href="https://x.com/Triple_Goats" class="social-icon-link" target="_blank" rel="noopener" aria-label="Twitter">
            <i class="fab fa-twitter"></i>
          </a>
          <a href="https://www.facebook.com/TripleGoats" class="social-icon-link" target="_blank" rel="noopener" aria-label="Facebook">
            <i class="fab fa-facebook-f"></i>
          </a>
          <a href="https://www.tiktok.com/@tg.auto.rwanda" class="social-icon-link" target="_blank" rel="noopener" aria-label="TikTok">
            <i class="fab fa-tiktok"></i>
          </a>
      </div>
    </nav>

    <!-- 桌面端社媒图标 -->
    <div class="top-social-media desktop-only">
      <a href="https://www.instagram.com/tg_auto_rwanda/" class="social-icon-link" target="_blank" rel="noopener" aria-label="Instagram">
        <i class="fab fa-instagram"></i>
      </a>
      <a href="https://x.com/Triple_Goats" class="social-icon-link" target="_blank" rel="noopener" aria-label="Twitter">
        <i class="fab fa-twitter"></i>
      </a>
      <a href="https://www.facebook.com/TripleGoats" class="social-icon-link" target="_blank" rel="noopener" aria-label="Facebook">
        <i class="fab fa-facebook-f"></i>
      </a>
      <a href="https://www.tiktok.com/@tg.auto.rwanda" class="social-icon-link" target="_blank" rel="noopener" aria-label="TikTok">
        <i class="fab fa-tiktok"></i>
      </a>
    </div>
  </header>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount, watch } from 'vue'

const menuOpen = ref(false)
const dropdownOpen = ref(false)

const toggleMenu = () => {
  menuOpen.value = !menuOpen.value
}

const closeMenu = () => {
  menuOpen.value = false
  dropdownOpen.value = false
}

watch(menuOpen, (val) => {
    if (val) {
        document.body.style.overflow = 'hidden'
    } else {
        document.body.style.overflow = ''
    }
})

const toggleDropdown = () => {
  if (window.innerWidth <= 768) {
    dropdownOpen.value = !dropdownOpen.value
  }
}

const handleClickOutside = (event) => {
  const dropdown = document.querySelector('.dropdown')
  const nav = document.querySelector('nav')
  const menuToggle = document.querySelector('.menu-toggle')
  if (dropdown && !dropdown.contains(event.target) && window.innerWidth <= 768) {
    dropdownOpen.value = false
  }
  if (menuOpen.value && nav && !nav.contains(event.target) && !menuToggle.contains(event.target)) {
      menuOpen.value = false;
  }
}

onMounted(() => {
  document.addEventListener('click', handleClickOutside)
  document.addEventListener('touchstart', handleClickOutside)
})

onBeforeUnmount(() => {
  document.removeEventListener('click', handleClickOutside)
  document.removeEventListener('touchstart', handleClickOutside)
  document.body.style.overflow = ''
})
</script>

<style scoped>
/* ========== 桌面端基础样式 ========== */
header {
    background: var(--primary-color);
    color: white;
    padding: 1rem 1.5rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: sticky;
    top: 0;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    z-index: 1000;
}

.logo {
    display: flex;
    align-items: center;
    gap: 1rem;
    text-decoration: none;
    color: white;
}

.logo img {
    width: 60px;
    height: 60px;
    object-fit: contain;
    border-radius: 50%;
    background: white;
    padding: 2px;
}

.logo-text h1 {
    font-size: 1.5rem;
    font-weight: 700;
    margin: 0;
    color: var(--accent-color);
    letter-spacing: -0.025em;
}

.logo .slogan {
    font-size: 0.75rem;
    font-weight: 600;
    color: var(--text-muted);
    letter-spacing: 0.05em;
    margin-top: 0.25rem;
}

nav {
    display: flex;
    align-items: center;
    gap: 2rem;
}

nav a {
    color: var(--text-color);
    font-weight: 500;
    font-size: 0.95rem;
    padding: 0.5rem 0;
    position: relative;
    transition: color 0.2s;
}

nav a:hover,
nav a.router-link-active {
    color: var(--accent-color);
}

nav a::after {
    content: '';
    position: absolute;
    width: 0;
    height: 2px;
    bottom: 0;
    left: 0;
    background-color: var(--accent-color);
    transition: width 0.3s ease;
}

nav a:hover::after,
nav a.router-link-active::after {
    width: 100%;
}

/* 下拉菜单 */
.dropdown {
    position: relative;
}

.dropbtn {
    cursor: pointer;
    font-weight: 500;
    display: flex;
    align-items: center;
    gap: 0.25rem;
}

.dropdown-content {
    display: none;
    position: absolute;
    top: 100%;
    left: 50%;
    transform: translateX(-50%);
    background-color: var(--card-bg-color);
    min-width: 180px;
    box-shadow: var(--shadow-lg);
    border-radius: 0.5rem;
    padding: 0.5rem 0;
    z-index: 1001;
    margin-top: 0.5rem;
    border: 1px solid rgba(255, 255, 255, 0.1);
}

.dropdown:hover .dropdown-content,
.dropdown.active .dropdown-content {
    display: block;
    animation: fadeIn 0.2s ease-out;
}

.dropdown-content a {
    display: block;
    padding: 0.75rem 1.5rem;
    color: var(--text-color);
    text-align: left;
    font-size: 0.9rem;
}

.dropdown-content a:hover {
    background-color: var(--card-hover-color);
    color: var(--accent-color);
}

/* 社媒图标 */
.top-social-media {
    display: flex;
    gap: 0.625rem;
    align-items: center;
}

.social-icon-link {
    width: 36px;
    height: 36px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.1);
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 1rem;
    transition: all 0.2s;
    text-decoration: none;
}

.social-icon-link:hover {
    background: var(--accent-color);
    transform: translateY(-2px);
    color: white;
}

/* 汉堡菜单按钮 */
.menu-toggle {
    display: none;
    position: relative;
    width: 28px;
    height: 20px;
    cursor: pointer;
    z-index: 1002;
    background: transparent;
    border: none;
    padding: 0;
}

.menu-toggle span {
    display: block;
    position: absolute;
    width: 100%;
    height: 2px;
    background-color: white;
    border-radius: 2px;
    transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
    left: 0;
    transform-origin: center center;
}

.menu-toggle span:nth-child(1) { top: 0; }
.menu-toggle span:nth-child(2) { top: 50%; transform: translateY(-50%); }
.menu-toggle span:nth-child(3) { bottom: 0; }

/* 移动端默认隐藏 */
.mobile-only { display: none; }

/* ========== 移动端适配 ========== */
@media (max-width: 768px) {
    header {
        padding: 0.75rem 1rem;
    }

    .logo img {
        width: 44px;
        height: 44px;
    }

    .logo-text h1 {
        font-size: 1.15rem;
    }

    .logo .slogan {
        font-size: 0.65rem;
    }

    /* 显示汉堡按钮，隐藏桌面端社媒 */
    .menu-toggle { display: flex; }
    .desktop-only { display: none !important; }

    /* X 形动画 */
    .menu-toggle.active span:nth-child(1) {
        top: 50%;
        transform: translateY(-50%) rotate(45deg);
    }
    .menu-toggle.active span:nth-child(2) {
        opacity: 0;
    }
    .menu-toggle.active span:nth-child(3) {
        top: 50%;
        bottom: auto;
        transform: translateY(-50%) rotate(-45deg);
    }

    /* 全屏导航菜单 */
    nav {
        position: fixed;
        top: 0;
        right: -100%;
        width: 100%;
        height: 100vh;
        background: rgba(15, 23, 42, 0.97);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        flex-direction: column;
        align-items: center;
        justify-content: flex-start;
        padding: 5rem 2rem 2rem;
        z-index: 1001;
        transition: right 0.35s cubic-bezier(0.4, 0, 0.2, 1);
        overflow-y: auto;
        gap: 0;
    }

    nav.active { right: 0; }

    /* 导航链接 */
    nav a {
        font-size: 1.35rem;
        font-weight: 600;
        margin: 0.8rem 0;
        width: 100%;
        text-align: center;
        letter-spacing: 0.05em;
        padding: 0.5rem 0;
    }

    nav a::after { display: none; }

    /* 下拉菜单 */
    .dropbtn {
        font-size: 1.35rem;
        font-weight: 600;
        letter-spacing: 0.05em;
        justify-content: center;
        width: 100%;
        padding: 0.8rem 0;
    }

    .dropdown-content {
        position: static;
        background: rgba(255, 255, 255, 0.05);
        box-shadow: none;
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 0.75rem;
        transform: none;
        text-align: center;
        padding: 0.25rem 0;
        margin: 0.25rem auto 0.5rem;
        display: none;
        width: 80%;
    }

    .dropdown.active .dropdown-content { display: block; }

    .dropdown-content a {
        font-size: 1.05rem;
        font-weight: 500;
        padding: 0.7rem 1rem;
        color: var(--text-muted);
        text-align: center;
        border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    }

    .dropdown-content a:last-child { border-bottom: none; }

    .dropdown-content a:hover {
        color: var(--accent-color);
        background: rgba(255, 255, 255, 0.03);
    }

    /* 移动端社媒图标 */
    .top-social-media { display: none; }

    .mobile-only {
        display: flex;
        justify-content: center;
        gap: 1rem;
        margin-top: 2rem;
        padding-top: 1.5rem;
        border-top: 1px solid rgba(255, 255, 255, 0.08);
        width: 80%;
    }

    .mobile-only .social-icon-link {
        width: 44px;
        height: 44px;
        font-size: 1.2rem;
    }
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px) translateX(-50%); }
    to { opacity: 1; transform: translateY(0) translateX(-50%); }
}
</style>

