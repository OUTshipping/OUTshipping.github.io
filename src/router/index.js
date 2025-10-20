import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      redirect: '/home'
    },
    {
      path: '/home',
      name: 'Home',
      component: () => import('@/views/HomeView.vue')
    },
    {
      path: '/about',
      name: 'About',
      component: () => import('@/views/AboutView.vue')
    },
    {
      path: '/inventory',
      name: 'Inventory',
      component: () => import('@/views/InventoryView.vue')
    },
    {
      path: '/contact',
      name: 'Contact',
      component: () => import('@/views/ContactView.vue')
    },
    {
      path: '/services',
      name: 'Services',
      component: () => import('@/views/ServicesView.vue')
    },
    {
      path: '/charging',
      name: 'Charging',
      component: () => import('@/views/ChargingView.vue')
    },
    {
      path: '/testdrive',
      name: 'TestDrive',
      component: () => import('@/views/TestDriveView.vue')
    },
    {
      path: '/rental',
      name: 'Rental',
      component: () => import('@/views/RentalView.vue')
    },
    {
      path: '/taxi',
      name: 'Taxi',
      component: () => import('@/views/TaxiView.vue')
    },
    {
      path: '/suv',
      name: 'SUV',
      component: () => import('@/views/SUVView.vue')
    },
    // 车辆详情页
    {
      path: '/song-plus',
      name: 'SongPlus',
      component: () => import('@/views/vehicles/SongPlusView.vue')
    },
    {
      path: '/byd-seagull',
      name: 'BYDSeagull',
      component: () => import('@/views/vehicles/BYDSeagullView.vue')
    },
    {
      path: '/byd-yuan-plus',
      name: 'BYDYuanPlus',
      component: () => import('@/views/vehicles/BYDYuanPlusView.vue')
    },
    {
      path: '/toyota-bz3',
      name: 'ToyotaBZ3',
      component: () => import('@/views/vehicles/ToyotaBZ3View.vue')
    },
    {
      path: '/id4-crozz',
      name: 'ID4Crozz',
      component: () => import('@/views/vehicles/ID4CrozzView.vue')
    },
    {
      path: '/leapmotor-c16',
      name: 'LeapmotorC16',
      component: () => import('@/views/vehicles/LeapmotorC16View.vue')
    },
    {
      path: '/kia-ev5',
      name: 'KIAEV5',
      component: () => import('@/views/vehicles/KIAEV5View.vue')
    },
    {
      path: '/farizon-v6e',
      name: 'FarizonV6E',
      component: () => import('@/views/vehicles/FarizonV6EView.vue')
    },
    {
      path: '/toyota-corolla-cross-frontlander',
      name: 'ToyotaFrontlander',
      component: () => import('@/views/vehicles/ToyotaFrontlanderView.vue')
    },
    {
      path: '/toyota-corolla-cross-highland',
      name: 'ToyotaHighland',
      component: () => import('@/views/vehicles/ToyotaHighlandView.vue')
    },
    {
      path: '/byd-tang-l',
      name: 'BYDTangL',
      component: () => import('@/views/vehicles/BYDTangLView.vue')
    },
    {
      path: '/farizon-v7e',
      name: 'FarizonV7E',
      component: () => import('@/views/vehicles/FarizonV7EView.vue')
    },
    {
      path: '/geely-randa',
      name: 'GeelyRanda',
      component: () => import('@/views/vehicles/GeelyRandaView.vue')
    },
    {
      path: '/toyota-bz3x',
      name: 'ToyotaBZ3X',
      component: () => import('@/views/vehicles/ToyotaBZ3XView.vue')
    },
    {
      path: '/leapmotor-c10',
      name: 'LeapmotorC10',
      component: () => import('@/views/vehicles/LeapmotorC10View.vue')
    },
    {
      path: '/icar-03',
      name: 'ICAR03',
      component: () => import('@/views/vehicles/ICAR03View.vue')
    },
    {
      path: '/icar-v23',
      name: 'ICARV23',
      component: () => import('@/views/vehicles/ICARV23View.vue')
    },
    {
      path: '/jetour-shanhai-t2',
      name: 'JetourShanhaiT2',
      component: () => import('@/views/vehicles/JetourShanhaiT2View.vue')
    }
  ],
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else {
      return { top: 0 }
    }
  }
})

export default router

