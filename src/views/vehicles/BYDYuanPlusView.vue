<template>
  <VehicleDetail
    vehicleName="2025 BYD YUAN PLUS"
    description="The BYD YUAN PLUS is a compact SUV designed for urban driving. It offers a range of 510 km, seating for up to 5 passengers, and a basic configuration. With its efficient electric motor and modern design, the YUAN PLUS is perfect for city commuters looking for a reliable and eco-friendly vehicle."
    :specs="{
      year: '2025',
      make: 'BYD',
      model: 'YUAN PLUS',
      range: '510',
      seats: '5',
      category: 'Basic',
      batteryCapacity: 'N/A'
    }"
    :images="[
      '/yuanplus/yuanplus (1).jpg',
      '/yuanplus/yuanplus (2).jpg',
      '/yuanplus/yuanplus (3).jpg',
      '/yuanplus/yuanplus (4).jpg',
      '/yuanplus/yuanplus (5).jpg',
      '/yuanplus/yuanplus (6).jpg',
      '/yuanplus/yuanplus (7).jpg'
    ]"
    :colors="['#808080']"
  />
</template>

<script setup>
import VehicleDetail from '@/components/VehicleDetail.vue'
</script>
