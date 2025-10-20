<template>
  <VehicleDetail
    vehicleName="2025 GEELY RADAR JINGGANG"
    description="The GEELY RADAR JINGGANG is a premium electric pickup truck combining rugged capability with advanced technology. It offers an impressive range of 550 km, comfortable seating for 5 passengers, and powerful performance. Perfect for those who need both work capability and modern electric vehicle features."
    :specs="{
      year: '2025',
      make: 'GEELY RADAR',
      model: 'JINGGANG',
      range: '550',
      seats: '5',
      category: 'Premium Pickup',
      batteryCapacity: '85 kWh'
    }"
    :images="[
      '/randa/randa.jpg',
      '/randa/randa (1).jpg',
      '/randa/randa (2).jpg',
      '/randa/randa (3).jpg',
      '/randa/randa (4).jpg',
      '/randa/randa (5).jpg',
      '/randa/randa (6).jpg',
      '/randa/randa (7).jpg',
      '/randa/randa (8).jpg',
      '/randa/randa (9).jpg',
      '/randa/randa (10).jpg',
      '/randa/randa (11).jpg',
      '/randa/randa (12).jpg',
      '/randa/randa (13).jpg'
    ]"
    :colors="['#000000', '#808080', '#FFFFFF']"
  />
</template>

<script setup>
import VehicleDetail from '@/components/VehicleDetail.vue'
</script>

