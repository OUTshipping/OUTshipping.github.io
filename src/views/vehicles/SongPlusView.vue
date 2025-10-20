<template>
  <VehicleDetail
    vehicleName="2025 BYD SONG PLUS"
    description="The BYD Song Plus is a versatile SUV designed for both family and commercial use. It comes with a 450 hp motor, offering a maximum range of 520 km and a spacious interior for up to 5 passengers. With advanced safety features and a sleek design, the Song Plus is perfect for various needs."
    :specs="{
      year: '2025',
      make: 'BYD',
      model: 'Song Plus',
      range: '520',
      seats: '5',
      category: 'PASSENGER',
      batteryCapacity: '71.7 kWh'
    }"
    :images="[
      '/songplus/songPLUS (1).jpg',
      '/songplus/songPLUS (1).png',
      '/songplus/songPLUS (2).png',
      '/songplus/songPLUS (3).png',
      '/songplus/songPLUS (4).png',
      '/songplus/songPLUS (5).png',
      '/songplus/songPLUS (6).png',
      '/songplus/songPLUS (7).png',
      '/songplus/songPLUS (8).png',
      '/songplus/songPLUS (9).png'
    ]"
    :colors="['#FFFFFF', '#000000', '#808080', '#D3D3D3']"
  />
</template>

<script setup>
import VehicleDetail from '@/components/VehicleDetail.vue'
</script>
