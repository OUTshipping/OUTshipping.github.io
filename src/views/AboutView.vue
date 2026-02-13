<template>
  <div class="about-page">
    <HeaderNav />
    
    <div class="hero">
      <h1>关于三羊汽车</h1>
      <p>了解我们的公司与价值观</p>
    </div>

    <main>
      <h2>关于三羊汽车</h2>
      <div class="about-section">
        <div class="section">
          <div class="section-content">
            <h3>我们的使命</h3>
            <p>三羊（卢旺达）汽车销售有限公司致力于为卢旺达市场提供高品质、多元化的汽车产品及优质的售后服务。我们的使命是为客户提供从轿车、SUV到皮卡和商用车的全系列车型选择，满足个人消费者、企业和政府部门的需求。我们致力于通过可靠的产品和卓越的服务，与客户建立长期合作关系。</p>
          </div>
        </div>
        <div class="section">
          <div class="section-content">
            <h3>我们的价值观</h3>
            <p>在三羊（卢旺达）汽车销售有限公司，我们秉持诚信、专业和以客户为中心的价值观。我们坚持以诚实和透明的方式经营业务，确保客户获得准确的信息和公正的对待。我们的专业团队致力于提供专业建议和支持，帮助客户做出明智的购车决策。我们以客户满意为首要目标，力求在每一次互动中超越期望。</p>
          </div>
        </div>
        <div class="section">
          <div class="section-content">
            <h3>我们的历史</h3>
            <p>三羊（卢旺达）汽车销售有限公司自成立以来，已发展成为卢旺达汽车行业的知名品牌。从最初的小型企业起步，我们不断扩大业务规模，如今服务于全国各地的广大客户。我们的发展历程始终以品质、创新和客户满意为核心，并将继续在业务的各个方面追求卓越。</p>
          </div>
        </div>
        <div class="section">
          <div class="section-content">
            <h3>社区参与</h3>
            <p>我们积极参与各类社区支持活动。我们与当地组织合作，推广道路安全意识和教育，致力于为所有人创造更安全的驾驶环境。此外，我们参与关注环境可持续发展和社会进步的企业社会责任项目，体现了我们在商业运营之外产生积极影响的决心。</p>
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
    background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('/about.jpg');
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
    text-align: left;
    padding-left: 20px;
}

.about-section {
    display: flex;
    flex-direction: column;
    gap: 30px;
    justify-content: center;
    padding: 50px 20px;
    background: var(--primary-color);
}

.section {
    background-color: #f5f5f5;
    padding: 2rem;
    margin: 2rem 0;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.section-content {
    background-color: #ffffff;
    padding: 1.5rem;
    border-radius: 8px;
    box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.05);
}

.section h3 {
    color: #2c3e50;
    font-size: 32px;
    margin: 0 0 1rem;
    border-bottom: 2px solid #0074d9;
    padding-bottom: 0.75rem;
}

.section p {
    color: #333333;
    font-size: 1rem;
    line-height: 1.6;
}

@media (max-width: 768px) {
    .about-section {
        padding: 20px 10px;
    }

    .section {
        margin: 1rem 0;
        padding: 1rem;
    }

    main {
        padding: 20px 10px;
    }
}

@media (max-width: 480px) {
    .about-section {
        padding: 10px;
    }

    .hero h1 {
        font-size: 36px;
    }
}
</style>

