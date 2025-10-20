<template>
  <VehicleDetail
    :vehicle-name="vehicleData.name"
    :description="vehicleData.description"
    :specs="vehicleData.specs"
    :images="vehicleData.images"
    :colors="vehicleData.colors"
  />
</template>

<script setup>
import VehicleDetail from '@/components/VehicleDetail.vue'

const vehicleData = {
  name: '2025 ID.4 CROZZ Pure Enjoyment Edition',
  description: 'The ID.4 CROZZ Pure Enjoyment Edition is an urban-friendly electric SUV that combines style, comfort, and efficiency. It features a 204hp electric motor, a range of up to 442km, and a spacious interior for up to 5 passengers. With its advanced safety features and modern design, it is the perfect choice for eco-conscious drivers who value both practicality and sustainability.',
  specs: {
    year: '2025',
    make: 'Volkswagen',
    model: 'ID.4 CROZZ Pure Enjoyment',
    range: '442',
    seats: '5',
    category: 'PASSENGER',
    batteryCapacity: '62.6 kWh'
  },
  images: [
    '/id4crozz/ID4 (1).jpg',
    '/id4crozz/ID4 (2).jpg',
    '/id4crozz/ID4 (3).jpg',
    '/id4crozz/ID4 (4).jpg',
    '/id4crozz/ID4 (5).jpg',
    '/id4crozz/ID4 (6).jpg',
    '/id4crozz/ID4 (7).jpg',
    '/id4crozz/ID4 (8).jpg'
  ],
  colors: ['#000000', '#0011ff']
}
</script>

