<template>
  <VehicleDetail
    vehicleName="2025 LEAPMOTOR C16"
    description="The LEAPMOTOR C16 is a premium SUV designed for comfort and long-distance travel. It offers an impressive range of 910 km, spacious seating for up to 6 passengers, and a luxurious interior. With advanced safety features and a sleek design, the C16 is perfect for families and those seeking a premium driving experience."
    :specs="{
      year: '2025',
      make: 'LEAPMOTOR',
      model: 'C16',
      range: '910',
      seats: '6',
      category: 'Premium',
      batteryCapacity: 'N/A'
    }"
    :images="[
      '/C16/C16 (1).jpg',
      '/C16/C16 (2).jpg',
      '/C16/C16 (3).jpg',
      '/C16/C16 (4).jpg',
      '/C16/C16 (5).jpg',
      '/C16/C16 (6).jpg',
      '/C16/C16 (7).jpg'
    ]"
    :colors="['#000000']"
  />
</template>

<script setup>
import VehicleDetail from '@/components/VehicleDetail.vue'
</script>
