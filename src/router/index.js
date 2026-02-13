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
      component: () => import('@/views/HomeView.vue'),
      meta: { title: 'Triple Goats — Rwanda\'s Premier Electric Vehicle Dealer', description: 'Shop BYD, Dongfeng, Leapmotor & more electric vehicles in Kigali. Full after-sales support, EV charging, taxi service and car rental.' }
    },
    {
      path: '/about',
      name: 'About',
      component: () => import('@/views/AboutView.vue'),
      meta: { title: 'About Us — Triple Goats | T&G Automobile Rwanda', description: 'Founded in 2023 in Kigali\'s Kicukiro district, Triple Goats is Rwanda\'s trusted EV dealer partnering with BYD, Dongfeng and more.' }
    },
    {
      path: '/inventory',
      name: 'Inventory',
      component: () => import('@/views/InventoryView.vue'),
      meta: { title: 'EV Inventory — Browse Electric Vehicles | Triple Goats', description: 'Explore our full range of electric sedans, SUVs, vans and trucks from BYD, Dongfeng, Leapmotor, Kia, Toyota and more.' }
    },
    {
      path: '/contact',
      name: 'Contact',
      component: () => import('@/views/ContactView.vue'),
      meta: { title: 'Contact Us — Triple Goats Kigali Showroom', description: 'Visit our Kigali showroom, call us, or send a WhatsApp message. Open Monday–Friday 8am–6pm, Saturday 9am–1pm.' }
    },
    {
      path: '/services',
      name: 'Services',
      component: () => import('@/views/ServicesView.vue'),
      meta: { title: 'Services — Car Sales, EV Charging, Taxi & Rental | Triple Goats', description: 'Comprehensive automotive services including EV sales, charging stations, electric taxi service and car rental in Kigali.' }
    },
    {
      path: '/charging',
      name: 'Charging',
      component: () => import('@/views/ChargingView.vue'),
      meta: { title: 'EV Charging Stations — Triple Goats Kigali', description: 'Find EV charging stations in Kigali. Fast and reliable charging for all electric vehicle brands.' }
    },
    {
      path: '/testdrive',
      name: 'TestDrive',
      component: () => import('@/views/TestDriveView.vue'),
      meta: { title: 'Schedule a Test Drive — Triple Goats', description: 'Book a free test drive at our Kigali showroom. Experience the instant torque and whisper-quiet cabin of our electric vehicles.' }
    },
    {
      path: '/rental',
      name: 'Rental',
      component: () => import('@/views/RentalView.vue'),
      meta: { title: 'Electric Car Rental — Triple Goats Kigali', description: 'Rent a fully charged EV for a day trip, business engagement, or anything in between. Short-term and long-term rentals available.' }
    },
    {
      path: '/taxi',
      name: 'Taxi',
      component: () => import('@/views/TaxiView.vue'),
      meta: { title: 'Electric Taxi Service — Triple Goats Kigali', description: 'Clean, quiet, and affordable electric taxi rides across Kigali. Professional drivers, air-conditioned cabins, zero emissions.' }
    },
    {
      path: '/suv',
      name: 'SUV',
      component: () => import('@/views/SUVView.vue'),
      meta: { title: 'Electric SUV Collection — Triple Goats', description: 'Explore our lineup of electric SUVs built for African terrain. Bold design, generous ground clearance, and advanced safety features.' }
    },
    // 动态车辆详情页
    {
      path: '/vehicle/:slug',
      name: 'VehicleDetail',
      component: () => import('@/views/VehicleDynamicView.vue'),
      meta: { title: 'Vehicle Details — Triple Goats', description: 'View detailed specs, photos and pricing for this electric vehicle at Triple Goats.' }
    },
    // 后台管理页面
    {
      path: '/admin',
      name: 'Admin',
      component: () => import('@/views/AdminView.vue'),
      meta: { title: 'Admin — Triple Goats' }
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

// 动态更新页面 title 和 meta description
const DEFAULT_TITLE = 'Triple Goats — Rwanda\'s Premier Electric Vehicle Dealer | Green Energy Green Life'
const DEFAULT_DESC = 'Shop BYD, Dongfeng, Leapmotor & more electric vehicles in Kigali. Full after-sales support, EV charging, taxi service and car rental.'

router.afterEach((to) => {
  document.title = to.meta.title || DEFAULT_TITLE
  const descTag = document.querySelector('meta[name="description"]')
  if (descTag) {
    descTag.setAttribute('content', to.meta.description || DEFAULT_DESC)
  }
})

export default router

