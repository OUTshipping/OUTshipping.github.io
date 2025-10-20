<template>
  <VehicleDetail
    vehicleName="2025 TOYOTA HIGHLAND"
    description="The Toyota Highland is a versatile SUV designed for both family and commercial use. It comes with a 450 hp motor, offering a maximum range of 530 km and a spacious interior for up to 5 passengers. With advanced safety features and a sleek design, the Highland is perfect for various needs."
    :specs="{
      year: '2025',
      make: 'Toyota',
      model: 'Highland',
      range: '530',
      seats: '5',
      category: 'SUV',
      batteryCapacity: 'N/A'
    }"
    :images="[
      '/highland/highland.jpg',
      '/highland/highland (1).jpg',
      '/highland/highland (2).jpg',
      '/highland/highland (3).jpg',
      '/highland/highland (4).jpg',
      '/highland/highland (5).jpg',
      '/highland/highland (6).jpg'
    ]"
    :colors="['#000000']"
  />
</template>

<script setup>
import VehicleDetail from '@/components/VehicleDetail.vue'
</script>
