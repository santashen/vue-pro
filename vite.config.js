import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  base: '/toy/',  // 👈 关键设置：让它适配 windsong.top/toy/
  plugins: [vue()]
})