<template>
  <VehicleDetail
    vehicleName="2025 TOYOTA BZ3X"
    description="The TOYOTA BZ3X is a premium electric SUV that combines Toyota's legendary reliability with cutting-edge electric technology. With a range of 580 km, seating for 5 passengers, and advanced safety systems, the BZ3X represents the future of sustainable mobility."
    :specs="{
      year: '2025',
      make: 'TOYOTA',
      model: 'BZ3X',
      range: '580',
      seats: '5',
      category: 'Premium SUV',
      batteryCapacity: '90 kWh'
    }"
    :images="[
      '/bz3x/bz3x.jpg',
      '/bz3x/bz3x (1).jpg',
      '/bz3x/bz3x (2).jpg',
      '/bz3x/bz3x (3).jpg',
      '/bz3x/bz3x (4).jpg',
      '/bz3x/bz3x (5).jpg',
      '/bz3x/bz3x (6).jpg',
      '/bz3x/bz3x (7).jpg',
      '/bz3x/bz3x (8).jpg',
      '/bz3x/bz3x (9).jpg',
      '/bz3x/bz3x (10).jpg',
      '/bz3x/bz3x (11).jpg',
      '/bz3x/bz3x (12).jpg',
      '/bz3x/bz3x (13).jpg',
      '/bz3x/bz3x (14).jpg'
    ]"
    :colors="['#FFFFFF', '#000000']"
  />
</template>

<script setup>
import VehicleDetail from '@/components/VehicleDetail.vue'
</script>

