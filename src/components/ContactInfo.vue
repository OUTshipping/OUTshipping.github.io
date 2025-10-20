<template>
  <div class="contact-info">
    <h3>Contact Us</h3>
    <p>
      <a href="https://wa.me/250785084313" target="_blank" class="whatsapp-link">Phone: +250 785 084 313</a> /
      <a href="https://wa.me/250794104908" target="_blank" class="whatsapp-link">+250 794 104 908</a>
    </p>
    <p>Email: tgautomobilee@gmail.com</p>
    <p>Address: KK 15 Rd, Kicukiro, Kigali</p>
    <router-link to="/testdrive" class="btn">Schedule a Test Drive</router-link>
  </div>
</template>

<script setup>
// 联系信息组件
</script>

<style scoped>
.contact-info {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 30px 20px;
    background: var(--primary-color);
    text-align: center;
}

.contact-info h3 {
    font-size: 24px;
    margin-bottom: 20px;
}

.contact-info p {
    text-align: center;
    margin-bottom: 15px;
}

.contact-info .btn {
    margin-top: 20px;
}

@media (max-width: 768px) {
    .contact-info {
        padding: 10px;
    }

    .contact-info h3 {
        font-size: 20px;
    }

    .contact-info p {
        font-size: 14px;
    }

    .contact-info .btn {
        font-size: 14px;
        padding: 10px 15px;
        margin-top: 10px;
    }
}
</style>

