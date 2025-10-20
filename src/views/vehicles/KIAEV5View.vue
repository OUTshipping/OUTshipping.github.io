<template>
  <VehicleDetail
    vehicleName="2025 KIA EV5"
    description="The KIA EV5 is a compact SUV designed for urban driving. It offers a range of 530 km, seating for up to 5 passengers, and a basic configuration. With its efficient electric motor and modern design, the EV5 is perfect for city commuters looking for a reliable and eco-friendly vehicle."
    :specs="{
      year: '2025',
      make: 'KIA',
      model: 'EV5',
      range: '530',
      seats: '5',
      category: 'Basic',
      batteryCapacity: 'N/A'
    }"
    :images="[
      '/EV5/EV5 (1).jpg',
      '/EV5/EV5 (2).jpg',
      '/EV5/EV5 (3).jpg',
      '/EV5/EV5 (4).jpg',
      '/EV5/EV5 (5).jpg',
      '/EV5/EV5 (6).jpg',
      '/EV5/EV5 (7).jpg',
      '/EV5/EV5 (8).jpg',
      '/EV5/EV5 (9).jpg',
      '/EV5/EV5 (10).jpg'
    ]"
    :colors="['#808080']"
  />
</template>

<script setup>
import VehicleDetail from '@/components/VehicleDetail.vue'
</script>
