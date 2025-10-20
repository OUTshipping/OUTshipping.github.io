<template>
  <header>
    <router-link to="/home" class="logo">
      <img src="/companylogo.jpg" alt="Triple Goats Logo" loading="lazy">
      <div class="logo-text">
        <h1>Triple Goats</h1>
        <p class="slogan">GREEN ENERGY GREEN LIFE</p>
      </div>
    </router-link>
    
    <nav id="nav-menu" :class="{ active: menuOpen }">
      <router-link to="/inventory" @click="closeMenu">INVENTORY</router-link>
      <router-link to="/charging" @click="closeMenu">CHARGING</router-link>
      <router-link to="/services" @click="closeMenu">SERVICES</router-link>
      <div class="dropdown" :class="{ active: dropdownOpen }">
        <a href="javascript:void(0)" class="dropbtn" @click.stop="toggleDropdown">DISCOVER</a>
        <div class="dropdown-content">
          <router-link to="/testdrive" @click="closeMenu">TEST DRIVE</router-link>
          <router-link to="/about" @click="closeMenu">ABOUT</router-link>
          <router-link to="/contact" @click="closeMenu">CONTACT</router-link>
        </div>
      </div>
    </nav>
    
    <div class="top-social-media">
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
    
    <div class="menu-toggle" :class="{ active: menuOpen }" @click="toggleMenu">
      <span></span>
      <span></span>
      <span></span>
    </div>
  </header>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'

const menuOpen = ref(false)
const dropdownOpen = ref(false)

const toggleMenu = () => {
  menuOpen.value = !menuOpen.value
}

const closeMenu = () => {
  menuOpen.value = false
  dropdownOpen.value = false
}

const toggleDropdown = () => {
  if (window.innerWidth <= 768) {
    dropdownOpen.value = !dropdownOpen.value
  }
}

const handleClickOutside = (event) => {
  const dropdown = document.querySelector('.dropdown')
  if (dropdown && !dropdown.contains(event.target) && window.innerWidth <= 768) {
    dropdownOpen.value = false
  }
}

onMounted(() => {
  document.addEventListener('click', handleClickOutside)
  document.addEventListener('touchstart', handleClickOutside)
})

onBeforeUnmount(() => {
  document.removeEventListener('click', handleClickOutside)
  document.removeEventListener('touchstart', handleClickOutside)
})
</script>

<style scoped>
header {
    background: var(--primary-color);
    color: var(--secondary-color);
    padding: 10px 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.logo {
    display: flex;
    align-items: center;
    transition: transform 0.3s, filter 0.3s;
}

.logo img {
    width: 80px;
    margin-right: 10px;
}

.logo .logo-text {
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.logo h1 {
    font-size: 36px;
    margin: 0 0 3px 0;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
    color: var(--accent-color);
}

.logo .slogan {
    font-size: 12px;
    font-weight: bold;
    text-transform: uppercase;
    color: var(--secondary-color);
    user-select: none;
    font-family: 'Roboto', sans-serif;
    margin-top: 0;
    text-shadow: 0 1px 2px rgba(0, 0, 0, 0.5);
}

.menu-toggle {
    display: none;
    flex-direction: column;
    cursor: pointer;
    padding: 5px;
}

.menu-toggle span {
    display: block;
    width: 25px;
    height: 3px;
    background-color: var(--secondary-color);
    margin: 4px 0;
    transition: transform 0.3s, background-color 0.3s;
}

.menu-toggle.active span:nth-child(1) {
    transform: rotate(45deg) translate(5px, 5px);
}

.menu-toggle.active span:nth-child(2) {
    opacity: 0;
}

.menu-toggle.active span:nth-child(3) {
    transform: rotate(-45deg) translate(5px, -5px);
}

nav {
    display: flex;
    gap: 15px;
    justify-content: center;
    flex-grow: 1;
}

nav a {
    color: var(--secondary-color);
    padding: 8px 15px;
    border-radius: 5px;
    transition: background-color 0.3s, transform 0.3s;
}

nav a:hover,
nav a.router-link-active {
    transform: scale(1.1);
    background: rgba(255, 255, 255, 0.1);
}

.dropdown {
    position: relative;
}

.dropdown .dropbtn {
    color: var(--secondary-color);
    padding: 8px 15px;
    border-radius: 5px;
    display: inline-block;
    transition: background-color 0.3s, transform 0.3s;
    cursor: pointer;
}

.dropdown:hover .dropbtn {
    transform: scale(1.1);
    background: rgba(255, 255, 255, 0.1);
}

.dropdown-content {
    display: none;
    position: absolute;
    background-color: #f9f9f9;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    z-index: 1000;
    width: 200px;
    text-align: center;
    border-radius: 5px;
    top: 100%;
    left: 0;
}

.dropdown:hover .dropdown-content {
    display: block;
}

.dropdown-content a {
    display: block;
    padding: 10px;
    text-align: center;
    border-bottom: 1px solid #ddd;
    font-size: 14px;
    color: var(--dark-color);
}

.dropdown-content a:last-child {
    border-bottom: none;
}

.dropdown-content a:hover {
    background-color: #ddd;
}

.top-social-media {
    display: flex;
    justify-content: center;
    gap: 15px;
    padding: 0;
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

@media (max-width: 768px) {
    .menu-toggle {
        display: flex;
    }

    nav {
        flex-direction: column;
        position: absolute;
        top: 60px;
        left: 0;
        width: 100%;
        background-color: rgba(0, 0, 0, 0.8);
        display: none;
        transition: all 0.3s ease;
        z-index: 1001;
    }

    nav.active {
        top: 81.5px;
        display: flex;
    }

    nav a {
        padding: 15px;
        text-align: center;
    }

    .dropdown-content {
        position: static;
        background-color: rgba(0, 0, 0, 0.5);
        box-shadow: none;
        width: 100%;
        text-align: center;
    }

    .dropdown-content a {
        padding: 15px;
        border-bottom: 1px solid #ddd;
        color: var(--secondary-color);
    }

    .dropdown-content {
        display: none;
    }

    .dropdown.active .dropdown-content {
        display: block;
    }

    .dropdown .dropbtn {
        margin-left: -15px;
        width: 100%;
    }

    .top-social-media {
        display: none;
    }
}

@media (max-width: 480px) {
    .logo img {
        width: 60px;
    }
    .logo h1 {
        font-size: 24px;
    }
    .logo .slogan {
        font-size: 8px;
    }
}
</style>

