<template>
  <VehicleDetail
    vehicleName="2025 TOYOTA BZ3"
    description="The TOYOTA BZ3 is a stylish and modern electric vehicle designed for urban driving. It comes with a 300 hp motor, offering a maximum range of 517 km and a sophisticated interior for up to 5 passengers. With advanced safety features and a sleek design, the BZ3 is perfect for urban environments and eco-conscious drivers."
    :specs="{
      year: '2025',
      make: 'TOYOTA',
      model: 'BZ3',
      range: '517',
      seats: '5',
      category: 'PASSENGER',
      batteryCapacity: '56.3 kWh'
    }"
    :images="[
      '/bz3/bz3.jpg',
      '/bz3/bz3 (2).jpg',
      '/bz3/bz3 (3).jpg',
      '/bz3/bz3 (4).jpg',
      '/bz3/bz3 (5).jpg',
      '/bz3/bz3 (6).jpg',
      '/bz3/bz3 (7).jpg',
      '/bz3/bz3 (8).jpg',
      '/bz3/bz3 (9).jpg',
      '/bz3/bz3 (10).jpg'
    ]"
    :colors="['#808080']"
  />
</template>

<script setup>
import VehicleDetail from '@/components/VehicleDetail.vue'
</script>
