<template>
  <VehicleDetail
    vehicleName="2025 TOYOTA COROLLA CROSS FRONTLANDER"
    description="The Toyota Corolla Cross Frontlander is a versatile SUV designed for both urban and off-road driving. It offers a range of 400 km, seating for up to 5 passengers, and a premium configuration. With its powerful engine and advanced safety features, the Corolla Cross Frontlander is perfect for families and adventurers alike."
    :specs="{
      year: '2025',
      make: 'Toyota',
      model: 'Corolla Cross Frontlander',
      range: '400',
      seats: '5',
      category: 'Premium',
      batteryCapacity: 'N/A'
    }"
    :images="[
      '/frontlander/frontlander.jpg',
      '/frontlander/frontlander (1).jpg',
      '/frontlander/frontlander (2).jpg',
      '/frontlander/frontlander (3).jpg',
      '/frontlander/frontlander (4).jpg',
      '/frontlander/frontlander (5).jpg',
      '/frontlander/frontlander (6).jpg'
    ]"
    :colors="['#000000']"
  />
</template>

<script setup>
import VehicleDetail from '@/components/VehicleDetail.vue'
</script>
