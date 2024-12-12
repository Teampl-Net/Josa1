import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';

export default defineConfig({
  plugins: [vue()],
  base: '/',  // 애플리케이션의 기본 경로 설정
  resolve: {
    alias: {
      '@': '/src',
    },
  },
  server: {
    https: false,  // HTTPS 비활성화
    port: 8085,     // 포트를 443으로 설정
  },
});


