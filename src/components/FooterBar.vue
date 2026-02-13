<template>
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <!-- Company Info -->
        <div class="footer-col">
            <h3 class="footer-logo">Triple Goats</h3>
            <p class="footer-desc">
                Rwanda's trusted electric vehicle dealer. We bring premium BYD, Dongfeng, and other new energy vehicles to East Africa — backed by professional after-sales service, EV charging, and a commitment to a greener future.
            </p>
        </div>

        <!-- Quick Links -->
        <div class="footer-col">
            <h4>Quick Links</h4>
            <ul>
                <li><router-link to="/home">Home</router-link></li>
                <li><router-link to="/inventory">Inventory</router-link></li>
                <li><router-link to="/charging">Charging</router-link></li>
                <li><router-link to="/services">Services</router-link></li>
                <li><router-link to="/taxi">Taxi Service</router-link></li>
                <li><router-link to="/rental">Car Rental</router-link></li>
            </ul>
        </div>

        <!-- Support -->
        <div class="footer-col">
            <h4>Support</h4>
            <ul>
                <li><router-link to="/testdrive">Test Drive</router-link></li>
                <li><router-link to="/contact">Contact Us</router-link></li>
                <li><router-link to="/about">About Us</router-link></li>
            </ul>
        </div>

        <!-- Contact -->
        <div class="footer-col">
            <h4>Contact</h4>
            <ul class="contact-list">
                <li><i class="fas fa-map-marker-alt"></i> KK 15 Rd, Kicukiro, Kigali</li>
                <li><i class="fas fa-envelope"></i> tgautomobilee@gmail.com</li>
                <li><i class="fas fa-phone"></i> +250 785 084 313</li>
            </ul>
            <div class="footer-socials">
                <a href="https://www.instagram.com/tg_auto_rwanda/" target="_blank" rel="noopener"><i class="fab fa-instagram"></i></a>
                <a href="https://x.com/Triple_Goats" target="_blank" rel="noopener"><i class="fab fa-twitter"></i></a>
                <a href="https://www.facebook.com/TripleGoats" target="_blank" rel="noopener"><i class="fab fa-facebook-f"></i></a>
                <a href="https://www.tiktok.com/@tg.auto.rwanda" target="_blank" rel="noopener"><i class="fab fa-tiktok"></i></a>
            </div>
        </div>

        <!-- Our Global Network（集团关联内链） -->
        <div class="footer-col">
            <h4>Our Global Network</h4>
            <ul class="network-list">
                <li>
                  <a href="https://www.zjaladin.com" target="_blank" rel="noopener">Zhejiang Aladdin Group</a>
                  <span class="network-desc">Our China HQ — sourced directly from the factory to ensure the best price</span>
                </li>
                <li>
                  <a href="https://www.aladinauto.com" target="_blank" rel="noopener">AladinAuto Platform</a>
                  <span class="network-desc">Check our global vehicle inventory — certified used cars & EVs exported from China</span>
                </li>
            </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <p>&copy; 2025 Triple Goats. All rights reserved. | Located in Kigali, Rwanda — Member of <a href="https://www.zjaladin.com" target="_blank" rel="noopener" class="footer-inline-link">Zhejiang Aladdin Group</a></p>
      </div>
    </div>
  </footer>
</template>

<script setup>
// Footer组件
</script>

<style scoped>
.site-footer {
    background-color: var(--primary-color);
    color: var(--text-muted);
    padding: 4rem 0 2rem;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.footer-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 3rem;
    margin-bottom: 3rem;
}

.footer-logo {
    color: white;
    font-size: 1.5rem;
    margin-bottom: 1rem;
    font-weight: 700;
}

.footer-desc {
    font-size: 0.9rem;
    line-height: 1.6;
}

h4 {
    color: white;
    font-size: 1.1rem;
    margin-bottom: 1.5rem;
    font-weight: 600;
}

ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

ul li {
    margin-bottom: 0.75rem;
}

ul li a {
    color: var(--text-muted);
    text-decoration: none;
    transition: color 0.2s;
    font-size: 0.95rem;
}

ul li a:hover {
    color: var(--accent-color);
}

.contact-list li {
    display: flex;
    align-items: flex-start;
    gap: 0.75rem;
    font-size: 0.9rem;
}

.contact-list i {
    color: var(--accent-color);
    margin-top: 0.25rem;
}

.network-list {
    list-style: none;
    padding: 0;
    margin: 0;
}

.network-list li {
    margin-bottom: 1rem;
}

.network-list a {
    color: var(--accent-color);
    text-decoration: none;
    font-weight: 600;
    font-size: 0.95rem;
    transition: color 0.2s;
}

.network-list a:hover {
    color: white;
}

.network-desc {
    display: block;
    font-size: 0.8rem;
    color: var(--text-muted);
    margin-top: 0.25rem;
    line-height: 1.4;
}

.footer-socials {
    display: flex;
    gap: 1rem;
    margin-top: 1.5rem;
}

.footer-socials a {
    width: 36px;
    height: 36px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.1);
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    transition: all 0.3s;
}

.footer-socials a:hover {
    background: var(--accent-color);
    transform: translateY(-3px);
}

.footer-bottom {
    text-align: center;
    padding-top: 2rem;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    font-size: 0.85rem;
}

.footer-inline-link {
    color: var(--accent-color);
    text-decoration: none;
    transition: color 0.2s;
}

.footer-inline-link:hover {
    color: white;
}
</style>

