<template>
  <VehicleDetail
    vehicleName="2025 BYD TANG L"
    description="The BYD TANG L is a premium large SUV designed for families and long-distance travel. It offers an impressive range of 600 km, spacious seating for up to 7 passengers, and a luxurious interior. With advanced safety features and powerful performance, the TANG L is perfect for those seeking comfort and capability."
    :specs="{
      year: '2025',
      make: 'BYD',
      model: 'TANG L',
      range: '600',
      seats: '7',
      category: 'Premium SUV',
      batteryCapacity: '108.8 kWh'
    }"
    :images="[
      '/tangl/tangl.jpg',
      '/tangl/tangl (1).jpg',
      '/tangl/tangl (2).jpg',
      '/tangl/tangl (3).jpg',
      '/tangl/tangl (4).jpg',
      '/tangl/tangl (5).jpg',
      '/tangl/tangl (6).jpg',
      '/tangl/tangl (7).jpg',
      '/tangl/tangl (8).jpg',
      '/tangl/tangl (9).jpg',
      '/tangl/tangl (10).jpg',
      '/tangl/tangl (11).jpg',
      '/tangl/tangl (12).jpg',
      '/tangl/tangl (13).jpg',
      '/tangl/tangl (14).jpg'
    ]"
    :colors="['#000000', '#FFFFFF', '#808080']"
  />
</template>

<script setup>
import VehicleDetail from '@/components/VehicleDetail.vue'
</script>

