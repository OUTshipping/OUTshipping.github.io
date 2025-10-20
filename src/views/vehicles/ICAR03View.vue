<template>
  <VehicleDetail
    vehicleName="2025 ICAR 03"
    description="The ICAR 03 is a youthful and stylish electric SUV designed for urban adventurers. It offers a range of 400 km, seating for 5 passengers, and vibrant color options. With its affordable price and fun-to-drive character, the ICAR 03 is perfect for young professionals and families."
    :specs="{
      year: '2025',
      make: 'ICAR',
      model: '03',
      range: '400',
      seats: '5',
      category: 'Compact SUV',
      batteryCapacity: '50.6 kWh'
    }"
    :images="[
      '/icar03/icar03.jpg',
      '/icar03/icar03 (1).jpg',
      '/icar03/icar03 (2).jpg',
      '/icar03/icar03 (3).jpg',
      '/icar03/icar03 (4).jpg',
      '/icar03/icar03 (5).jpg',
      '/icar03/icar03 (6).jpg',
      '/icar03/icar03 (7).jpg',
      '/icar03/icar03 (8).jpg',
      '/icar03/icar03 (9).jpg',
      '/icar03/icar03 (10).jpg'
    ]"
    :colors="['#FF6B6B', '#4ECDC4', '#FFE66D']"
  />
</template>

<script setup>
import VehicleDetail from '@/components/VehicleDetail.vue'
</script>

