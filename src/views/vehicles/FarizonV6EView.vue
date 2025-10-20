<template>
  <VehicleDetail
    vehicleName="2025 FARIZON V6E"
    description="Farizon V6E is an electric light truck designed for urban logistics. It offers a spacious cargo area, a range of up to 305 km, and advanced safety features. Ideal for businesses looking for efficient and eco-friendly transportation solutions."
    :specs="{
      year: '2025',
      make: 'Farizon',
      model: 'V6E',
      range: '305',
      seats: '6',
      category: 'COMMERCIAL',
      batteryCapacity: '72 kWh'
    }"
    :images="[
      '/V6E/V6E (1).jpg',
      '/V6E/V6E (2).jpg',
      '/V6E/V6E (3).jpg',
      '/V6E/V6E (4).jpg',
      '/V6E/V6E (5).jpg',
      '/V6E/V6E (6).jpg',
      '/V6E/V6E (7).jpg'
    ]"
    :colors="['#FFFFFF']"
  />
</template>

<script setup>
import VehicleDetail from '@/components/VehicleDetail.vue'
</script>
