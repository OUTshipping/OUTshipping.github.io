<template>
  <VehicleDetail
    vehicleName="2025 BYD SEAGULL"
    description="The BYD SEAGULL is a compact SUV designed for urban driving. It offers a range of 300 km, seating for up to 5 passengers, and a basic configuration. With its efficient electric motor and modern design, the SEAGULL is perfect for city commuters looking for a reliable and eco-friendly vehicle."
    :specs="{
      year: '2025',
      make: 'BYD',
      model: 'SEAGULL',
      range: '300',
      seats: '5',
      category: 'Basic',
      batteryCapacity: 'N/A'
    }"
    :images="[
      '/seagull/SEAGULL (1).jpg',
      '/seagull/SEAGULL (2).jpg',
      '/seagull/SEAGULL (3).jpg',
      '/seagull/SEAGULL (4).jpg',
      '/seagull/SEAGULL (5).jpg',
      '/seagull/SEAGULL (6).jpg',
      '/seagull/SEAGULL (7).jpg'
    ]"
    :colors="['#000000']"
  />
</template>

<script setup>
import VehicleDetail from '@/components/VehicleDetail.vue'
</script>
