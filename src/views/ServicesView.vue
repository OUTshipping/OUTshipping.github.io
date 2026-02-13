<template>
  <div class="services-page">
    <HeaderNav />
    
    <div class="hero">
      <h1>我们的服务</h1>
      <p>了解我们提供的全方位服务</p>
    </div>

    <main>
      <h2>可用服务</h2>
      <div class="service-section">
        <div class="service-item">
          <div class="service-item-content">
            <router-link to="/inventory">
              <div>
                <h3>汽车销售<span class="arrow">→</span></h3>
                <p>浏览我们丰富的新车库存。我们提供轿车、SUV、卡车等多种车型，满足您的各种需求。</p>
              </div>
            </router-link>
          </div>
        </div>
        <div class="service-item">
          <div class="service-item-content">
            <router-link to="/charging">
              <div>
                <h3>电动车充电<span class="arrow">→</span></h3>
                <p>快速高效的电动汽车充电站，为您提供便捷的充电解决方案。</p>
              </div>
            </router-link>
          </div>
        </div>
        <div class="service-item">
          <div class="service-item-content">
            <router-link to="/taxi">
              <div>
                <h3>出租车服务<span class="arrow">→</span></h3>
                <p>便捷可靠的出租车服务，满足您的日常出行需求。我们的车队现代化且维护良好，确保舒适的乘车体验。</p>
              </div>
            </router-link>
          </div>
        </div>
        <div class="service-item">
          <div class="service-item-content">
            <router-link to="/rental">
              <div>
                <h3>汽车租赁<span class="arrow">→</span></h3>
                <p>灵活安全的汽车租赁选择。无论您需要一天还是一周的用车，我们都能满足。</p>
              </div>
            </router-link>
          </div>
        </div>
      </div>
    </main>

    <ContactInfo />
    <SocialMedia />
    <FooterBar />
  </div>
</template>

<script setup>
import HeaderNav from '@/components/HeaderNav.vue'
import FooterBar from '@/components/FooterBar.vue'
import SocialMedia from '@/components/SocialMedia.vue'
import ContactInfo from '@/components/ContactInfo.vue'
</script>

<style scoped>
.hero {
    position: relative;
    height: 60vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    color: var(--secondary-color);
    text-align: center;
    background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('/services.jpg');
    background-size: cover;
    background-position: center;
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

main {
    padding: 50px 20px;
    background: var(--primary-color);
    text-align: center;
}

main h2 {
    text-align: center;
    margin-bottom: 20px;
}

.service-section {
    display: flex;
    flex-direction: column;
    gap: 30px;
    justify-content: center;
    padding: 50px 20px;
    background: var(--primary-color);
    max-width: 1000px;
    margin: 0 auto;
}

.service-item {
    display: flex;
    align-items: center;
    padding: 25px;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 15px;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s, box-shadow 0.3s;
}

.service-item:hover {
    transform: translateY(-10px);
    box-shadow: 0 12px 30px rgba(0, 0, 0, 0.2);
}

.service-item-content {
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: left;
    margin-left: 15px;
    flex: 1;
}

.service-item-content a {
    display: flex;
    align-items: center;
    color: inherit;
    text-decoration: none;
    width: 100%;
}

.service-item-content a .arrow {
    margin-left: 10px;
    font-size: 22px;
    transition: transform 0.3s;
    color: var(--accent-color);
}

.service-item-content a:hover .arrow {
    transform: translateX(5px);
}

.service-item h3 {
    font-size: 28px;
    color: var(--secondary-color);
    text-align: center;
    margin: 0;
    display: flex;
    align-items: center;
    justify-content: center;
}

.service-item h3 .arrow {
    margin-left: 10px;
    color: var(--accent-color);
}

.service-item p {
    font-size: 18px;
    color: var(--secondary-color);
    line-height: 1.6;
    margin-bottom: 20px;
    opacity: 0.9;
}
</style>

