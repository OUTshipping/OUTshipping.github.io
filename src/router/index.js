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
    // 动态车辆详情页
    {
      path: '/vehicle/:slug',
      name: 'VehicleDetail',
      component: () => import('@/views/VehicleDynamicView.vue')
    },
    // 后台管理页面
    {
      path: '/admin',
      name: 'Admin',
      component: () => import('@/views/AdminView.vue')
    },
    // 旧路径兼容重定向
    { path: '/song-plus', redirect: '/vehicle/song-plus' },
    { path: '/farizon-v6e', redirect: '/vehicle/farizon-v6e' },
    { path: '/toyota-bz3', redirect: '/vehicle/toyota-bz3' },
    { path: '/id4-crozz', redirect: '/vehicle/id4-crozz' },
    { path: '/leapmotor-c16', redirect: '/vehicle/leapmotor-c16' },
    { path: '/kia-ev5', redirect: '/vehicle/kia-ev5' },
    { path: '/byd-seagull', redirect: '/vehicle/byd-seagull' },
    { path: '/byd-yuan-plus', redirect: '/vehicle/byd-yuan-plus' },
    { path: '/toyota-corolla-cross-frontlander', redirect: '/vehicle/toyota-corolla-cross-frontlander' },
    { path: '/toyota-corolla-cross-highland', redirect: '/vehicle/toyota-corolla-cross-highland' },
    { path: '/byd-tang-l', redirect: '/vehicle/byd-tang-l' },
    { path: '/farizon-v7e', redirect: '/vehicle/farizon-v7e' },
    { path: '/geely-randa', redirect: '/vehicle/geely-randa' },
    { path: '/toyota-bz3x', redirect: '/vehicle/toyota-bz3x' },
    { path: '/leapmotor-c10', redirect: '/vehicle/leapmotor-c10' },
    { path: '/icar-03', redirect: '/vehicle/icar-03' },
    { path: '/icar-v23', redirect: '/vehicle/icar-v23' },
    { path: '/jetour-shanhai-t2', redirect: '/vehicle/jetour-shanhai-t2' }
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

