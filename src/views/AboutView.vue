<template>
  <div class="about-page">
    <HeaderNav />
    
    <div class="hero">
      <h1>About T&G AUTOMOBILE</h1>
      <p>Learn more about our company and values</p>
    </div>

    <main>
      <h2>About T&G AUTOMOBILE</h2>
      <div class="about-section">
        <div class="section">
          <div class="section-content">
            <h3>Our Mission</h3>
            <p>San Yang (Rwanda) Automobile Sales Co., Ltd. is committed to providing high-quality and diverse automobile products as well as excellent after-sales services to the Rwandan market. Our mission is to offer customers a wide range of vehicle choices, from sedans and SUVs to pickup trucks and commercial vehicles, ensuring that we meet the needs of individual consumers, businesses, and government departments. We are dedicated to building long-term relationships with our customers by providing reliable products and exceptional service.</p>
          </div>
        </div>
        <div class="section">
          <div class="section-content">
            <h3>Our Values</h3>
            <p>At San Yang (Rwanda) Automobile Sales Co., Ltd., we uphold the values of integrity, professionalism, and customer-centricity. We believe in conducting our business with honesty and transparency, ensuring that our customers receive accurate information and fair treatment. Our team of professionals is committed to providing expert advice and support, helping customers make informed decisions about their vehicle purchases. We prioritize customer satisfaction and strive to exceed expectations in every interaction.</p>
          </div>
        </div>
        <div class="section">
          <div class="section-content">
            <h3>Our History</h3>
            <p>Founded in [specific year of establishment], San Yang (Rwanda) Automobile Sales Co., Ltd. has grown to become a trusted name in the Rwandan automobile industry. Starting as a small venture, we have expanded our operations and now serve a wide range of customers across the country. Our journey has been marked by a commitment to quality, innovation, and customer satisfaction, and we continue to strive for excellence in all aspects of our business.</p>
          </div>
        </div>
        <div class="section">
          <div class="section-content">
            <h3>Community Involvement</h3>
            <p>We are actively involved in supporting the local community through various initiatives. We collaborate with local organizations to promote road safety awareness and education, aiming to create a safer driving environment for everyone. Additionally, we participate in corporate social responsibility programs that focus on environmental sustainability and social development, reflecting our dedication to making a positive impact beyond our business operations.</p>
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

