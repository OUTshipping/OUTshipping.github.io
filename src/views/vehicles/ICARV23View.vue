<template>
  <VehicleDetail
    vehicleName="2025 ICAR V23"
    description="The ICAR V23 is a practical electric van designed for both commercial and family use. It offers a range of 380 km, spacious seating for 6 passengers, and versatile cargo configurations. Perfect for small businesses and growing families who need space and efficiency."
    :specs="{
      year: '2025',
      make: 'ICAR',
      model: 'V23',
      range: '380',
      seats: '6',
      category: 'Multi-purpose Van',
      batteryCapacity: '65 kWh'
    }"
    :images="[
      '/icarv23/icarv23.jpg',
      '/icarv23/icarv23 (1).jpg',
      '/icarv23/icarv23 (2).jpg',
      '/icarv23/icarv23 (3).jpg',
      '/icarv23/icarv23 (4).jpg',
      '/icarv23/icarv23 (5).jpg',
      '/icarv23/icarv23 (6).jpg',
      '/icarv23/icarv23 (7).jpg',
      '/icarv23/icarv23 (8).jpg',
      '/icarv23/icarv23 (9).jpg',
      '/icarv23/icarv23 (10).jpg'
    ]"
    :colors="['#FFFFFF', '#000000']"
  />
</template>

<script setup>
import VehicleDetail from '@/components/VehicleDetail.vue'
</script>

