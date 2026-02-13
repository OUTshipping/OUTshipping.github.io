<template>
  <header>
    <router-link to="/home" class="logo">
      <img src="/companylogo.jpg" alt="Triple Goats Logo" loading="lazy">
      <div class="logo-text">
        <h1>Triple Goats</h1>
        <p class="slogan">GREEN ENERGY GREEN LIFE</p>
      </div>
    </router-link>

    <!-- Mobile Menu Toggle -->
    <div class="menu-toggle" :class="{ active: menuOpen }" @click="toggleMenu" aria-label="Toggle Menu">
      <span></span>
      <span></span>
      <span></span>
    </div>

    <!-- Main Navigation -->
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
          <router-link to="/about" @click="closeMenu">ABOUT</router-link>
          <router-link to="/contact" @click="closeMenu">CONTACT</router-link>
        </div>
      </div>

      <!-- Mobile Socials (duplicated for better UX) -->
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

    <!-- Desktop Socials -->
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

// Lock body scroll when menu is open
watch(menuOpen, (val) => {
    if (val) {
        document.body.style.overflow = 'hidden'
    } else {
        document.body.style.overflow = ''
    }
})

const toggleDropdown = () => {
  // Only toggle on mobile or click interaction
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

  // Close menu if clicking outside on mobile
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

/* Dropdown */
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

.menu-toggle {
    display: none;
    position: relative;
    width: 32px;
    height: 24px;
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
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    left: 0;
    transform-origin: center center;
}

.menu-toggle span:nth-child(1) {
    top: 0;
}

.menu-toggle span:nth-child(2) {
    top: 50%;
    transform: translateY(-50%);
}

.menu-toggle span:nth-child(3) {
    bottom: 0;
}

/* Mobile Styles */
@media (max-width: 768px) {
    .menu-toggle {
        display: flex;
    }

    nav {
        position: fixed;
        top: 0;
        right: -100%;
        width: 100%;
        height: 100vh;
        background-color: rgba(15, 23, 42, 0.98);
        backdrop-filter: blur(10px);
        flex-direction: column;
        justify-content: center;
        transition: right 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        padding: 2rem;
        z-index: 1001;
    }

    nav.active {
        right: 0;
    }

    nav a {
        font-size: 1.5rem;
        margin: 1rem 0;
    }

    .dropdown-content {
        position: static;
        background: transparent;
        box-shadow: none;
        border: none;
        transform: none;
        text-align: center;
        padding-top: 0;
        margin-top: 0;
        display: none;
    }

    .dropdown.active .dropdown-content {
        display: block;
    }

    .dropdown-content a {
        font-size: 1.2rem;
        padding: 0.5rem;
        color: var(--text-muted);
    }

    .top-social-media {
        display: none; /* Consider moving inside nav for mobile */
    }

    .menu-toggle.active span:nth-child(1) {
        transform: rotate(45deg) translate(5px, 5px);
    }

    .menu-toggle.active span:nth-child(2) {
        opacity: 0;
    }

    .menu-toggle.active span:nth-child(3) {
        transform: rotate(-45deg) translate(5px, -6px);
    }

    .desktop-only {
        display: none !important;
    }
}

.mobile-only {
    display: none;
}

@media (max-width: 768px) {
    .mobile-only {
        display: flex;
        justify-content: center;
        margin-top: 2rem;
    }

    .mobile-only .social-icon-link {
        width: 44px;
        height: 44px;
        font-size: 1.25rem;
    }
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px) translateX(-50%); }
    to { opacity: 1; transform: translateY(0) translateX(-50%); }
}

/* Fixed Mobile Styles & Animation Override */
@media (max-width: 768px) {
    nav {
        justify-content: flex-start;
        padding: 6rem 2rem 2rem;
        backdrop-filter: blur(20px);
        background-color: rgba(15, 23, 42, 0.95);
        overflow-y: auto;
    }

    nav a {
        font-weight: 600;
        margin: 1.25rem 0;
        width: 100%;
        text-align: center;
    }

    .dropdown-content {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 0.75rem;
        width: 90%;
        margin: 0.5rem auto;
    }

    .dropdown-content a {
        border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        padding: 0.75rem;
    }

    .dropdown-content a:last-child {
        border-bottom: none;
    }

    /* Animation Fixes */
    .menu-toggle.active span:nth-child(1) {
        top: 50%;
        transform: translateY(-50%) rotate(45deg);
    }

    .menu-toggle.active span:nth-child(2) {
        opacity: 0;
    }

    .menu-toggle.active span:nth-child(3) {
        bottom: 50%;
        transform: translateY(50%) rotate(-45deg);
    }
}
</style>

