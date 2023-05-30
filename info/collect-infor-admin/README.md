# Vue 3 + Typescript + Vite

This template should help get you started developing with Vue 3 and Typescript in Vite. The template uses Vue 3 `<script setup>` SFCs, check out the [script setup docs](https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup) to learn more.

## Recommended IDE Setup

- [VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=johnsoncodehk.volar)

## Type Support For `.vue` Imports in TS

Since TypeScript cannot handle type information for `.vue` imports, they are shimmed to be a generic Vue component type by default. In most cases this is fine if you don't really care about component prop types outside of templates. However, if you wish to get actual prop types in `.vue` imports (for example to get props validation when using manual `h(...)` calls), you can enable Volar's `.vue` type support plugin by running `Volar: Switch TS Plugin on/off` from VSCode command palette.

## 启动部署

### 环境准备

- 安装 Node

  版本：≥v14.0.0

- 开发工具

  VSCode

- 必装插件

  - Vue Language Features (Volar) 
  - TypeScript Vue Plugin (Volar)

### 项目启动

1. npm install
2. npm run dev
3. 访问 http://localhost:3000

### 项目部署

- 本地打包

  ```
  npm run build:prod
  ```

  生成的静态文件位于项目根目录 dist 文件夹下

- 上传文件

  创建 `/usr/local/nginx/html/vue3` 目录，将打包生成 dist 的所有文件拷贝至此工作目录下
