import { ViteSSG } from 'vite-ssg'
import App from './App.vue'
import routes from './router'
import './assets/styles/global.css'

export const createApp = ViteSSG(
  App,
  {
    routes,
    scrollBehavior(to, from, savedPosition) {
      if (savedPosition) {
        return savedPosition
      } else {
        return { top: 0 }
      }
    }
  },
  ({ app, router, isClient }) => {
    // 客户端专用逻辑可在此添加
  }
)

