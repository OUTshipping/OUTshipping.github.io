<template>
  <VehicleDetail
    vehicleName="2025 FARIZON V7E"
    description="The FARIZON V7E is a versatile electric van designed for commercial and family use. It offers a range of 350 km, spacious seating for up to 7 passengers, and excellent cargo capacity. Ideal for businesses and large families seeking an efficient and practical electric vehicle."
    :specs="{
      year: '2025',
      make: 'FARIZON',
      model: 'V7E',
      range: '350',
      seats: '7',
      category: 'Commercial Van',
      batteryCapacity: '80 kWh'
    }"
    :images="[
      '/v7e/v7e.jpg',
      '/v7e/v7e (1).jpg',
      '/v7e/v7e (2).jpg',
      '/v7e/v7e (3).jpg',
      '/v7e/v7e (4).jpg',
      '/v7e/v7e (5).jpg',
      '/v7e/v7e (6).jpg',
      '/v7e/v7e (7).jpg',
      '/v7e/v7e (8).jpg',
      '/v7e/v7e (9).jpg',
      '/v7e/v7e (10).jpg',
      '/v7e/v7e (11).jpg',
      '/v7e/v7e (12).jpg',
      '/v7e/v7e (13).jpg',
      '/v7e/v7e (14).jpg'
    ]"
    :colors="['#FFFFFF']"
  />
</template>

<script setup>
import VehicleDetail from '@/components/VehicleDetail.vue'
</script>

