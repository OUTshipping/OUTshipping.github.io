import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { fileURLToPath, URL } from 'node:url'
import fs from 'node:fs'

export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server: {
    port: 3000
  },
  ssgOptions: {
    script: 'async',
    formatting: 'minify',
    includedRoutes(paths) {
      // 读取 vehicles.json 生成动态车辆路由
      const vehiclesJson = fs.readFileSync('./public/data/vehicles.json', 'utf-8')
      const vehicles = JSON.parse(vehiclesJson)
      const vehicleRoutes = vehicles
        .filter(v => v.enabled)
        .map(v => `/vehicle/${v.slug}`)

      // 排除 admin 页面、动态路由模板（含 :）和重定向路由，不需要预渲染
      const filtered = paths.filter(p =>
        p !== '/admin' &&
        !p.includes(':') &&
        !vehicles.some(v => p === `/${v.slug}`) &&
        p !== '/'
      )
      return [...filtered, ...vehicleRoutes]
    }
  }
})

