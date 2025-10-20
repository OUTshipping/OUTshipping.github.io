<template>
  <VehicleDetail
    vehicleName="2025 JETOUR SHANHAI T2"
    description="The JETOUR SHANHAI T2 is a rugged electric pickup truck designed for both work and adventure. It offers a range of 420 km, seating for 5 passengers, and impressive towing capacity. With its durable construction and off-road capability, the SHANHAI T2 is perfect for those who demand versatility."
    :specs="{
      year: '2025',
      make: 'JETOUR',
      model: 'SHANHAI T2',
      range: '420',
      seats: '5',
      category: 'Electric Pickup',
      batteryCapacity: '75 kWh'
    }"
    :images="[
      '/shanhait2/shanhait2.jpg',
      '/shanhait2/shanhait2 (1).jpg',
      '/shanhait2/shanhait2 (2).jpg',
      '/shanhait2/shanhait2 (3).jpg',
      '/shanhait2/shanhait2 (4).jpg',
      '/shanhait2/shanhait2 (5).jpg',
      '/shanhait2/shanhait2 (6).jpg',
      '/shanhait2/shanhait2 (7).jpg',
      '/shanhait2/shanhait2 (8).jpg',
      '/shanhait2/shanhait2 (9).jpg',
      '/shanhait2/shanhait2 (10).jpg',
      '/shanhait2/shanhait2 (11).jpg',
      '/shanhait2/shanhait2 (12).jpg'
    ]"
    :colors="['#000000', '#FFFFFF']"
  />
</template>

<script setup>
import VehicleDetail from '@/components/VehicleDetail.vue'
</script>

