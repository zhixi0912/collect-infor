import { fileURLToPath, URL } from 'node:url'
import { defineConfig, loadEnv } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig(({mode}) => {
  const env = loadEnv(mode, process.cwd(), '')
  return {
    plugins: [vue()],
    resolve: {
      alias: {
        '@': fileURLToPath(new URL('./src', import.meta.url)),
        'pub': fileURLToPath(new URL('./public', import.meta.url))
      }
    },
    // baseUrl: process.env.NODE_ENV === 'production' ? './' : '/',
    // 本地反向代理解决浏览器跨域限制
    server: {
      // host: '0.0.0.0',
      // port: Number(env.VITE_APP_PORT),
      host: '127.0.0.1',
      port: 8080,
      open: true, // 运行自动打开浏览器
      proxy: {
        [env.VITE_APP_BASE_API]: {
          target: env.VITE_APP_BASE_URL,
          // target: 'http://10.0.12.8:9500',
          // target: 'http://43.139.138.4:9500',
          // target: 'http://127.0.0.1:5000',
          changeOrigin: true,
          rewrite: path =>
            path.replace(new RegExp('^' + env.VITE_APP_BASE_API), '')
        }
      }
    },
    // build: {
    //   terserOptions: {
    //     compress: {
    //       drop_console: true,
    //       drop_debugger: true
    //     }
    //   }
    // }
  }
})
