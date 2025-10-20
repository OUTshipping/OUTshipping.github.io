<template>
  <VehicleDetail
    vehicleName="2025 LEAPMOTOR C10"
    description="The LEAPMOTOR C10 is a smart electric SUV designed for modern drivers. It offers a range of 530 km, comfortable seating for 5 passengers, and innovative technology features. With its sleek design and competitive pricing, the C10 is an excellent choice for tech-savvy buyers."
    :specs="{
      year: '2025',
      make: 'LEAPMOTOR',
      model: 'C10',
      range: '530',
      seats: '5',
      category: 'Smart SUV',
      batteryCapacity: '69.9 kWh'
    }"
    :images="[
      '/c10/c10.jpg',
      '/c10/c10 (1).jpg',
      '/c10/c10 (2).jpg',
      '/c10/c10 (3).jpg',
      '/c10/c10 (4).jpg',
      '/c10/c10 (5).jpg',
      '/c10/c10 (6).jpg',
      '/c10/c10 (7).jpg',
      '/c10/c10 (8).jpg',
      '/c10/c10 (9).jpg',
      '/c10/c10 (10).jpg'
    ]"
    :colors="['#808080', '#000000']"
  />
</template>

<script setup>
import VehicleDetail from '@/components/VehicleDetail.vue'
</script>

