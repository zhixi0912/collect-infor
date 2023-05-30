<template>
  <div class="sidebar-logo-container">
    <transition name="sidebarLogoFade">
      <router-link key="expand" class="sidebar-logo-link" to="/">
        <img :src="logo" class="sidebar-logo" />
        <h1 class="sidebar-title">信息管理平台</h1>
      </router-link>
    </transition>
  </div>
</template>

<script setup lang="ts">
import { reactive, toRefs } from 'vue';

const state = reactive({
  logo: new URL(`@/assets/kg.ico`, import.meta.url).href
})
const { logo } = toRefs(state);
</script>

<style lang="scss" scoped>
.sidebarLogoFade-enter-active {
  transition: opacity 1.5s;
}

.sidebarLogoFade-enter,
.sidebarLogoFade-leave-to {
  opacity: 0;
}
.hideSidebar {
  .sidebar-logo-container {
    padding-left: 10px;
  }
}
.sidebar-logo-container {
  position: relative;
  width: 100%;
  height: 50px;
  line-height: 50px;
  background: #2b2f3a;
  // text-align: center;
  padding-left: 20px;
  overflow: hidden;

  & .sidebar-logo-link {
    height: 100%;
    width: 100%;

    & .sidebar-logo {
      // width: 20px;
      // height: 20px;
      vertical-align: middle;
    }

    & .sidebar-title {
      display: inline-block;
      margin: 0;
      color: #fff;
      font-weight: 600;
      line-height: 50px;
      font-size: 14px;
      font-family: Avenir, Helvetica Neue, Arial, Helvetica, sans-serif;
      vertical-align: middle;
      margin-left: 12px;
    }
  }

  &.collapse {
    .sidebar-logo {
      margin-right: 0px;
    }
  }
}
</style>
