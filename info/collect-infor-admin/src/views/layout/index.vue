<template>
  <div :class="classObj" class="app-wrapper">
    <Sidebar class="sidebar-container" />
    <div class="main-container">
      <!-- <div class="fixed-header"> -->
      <div>
        <Navbar />
      </div>
      <AppMain />
    </div>
  </div>
</template>

<script lang="ts" setup>
import { computed } from 'vue';
import AppMain from './components/AppMain.vue';
import Navbar from './components/Navbar.vue'
import Sidebar from './components/Sidebar/index.vue'
import useStore from '@/stores/index';

const { sidebar } = useStore();
const classObj = computed(() => ({
  hideSidebar: sidebar.isCollapse,
  openSidebar: !sidebar.isCollapse,
}));
</script>

<style lang="scss" scoped>
// @import '@/styles/main.scss';
.app-wrapper {
  // @include clearfix;
  position: relative;
  height: 100%;
  width: 100%;

  &.mobile.openSidebar {
    position: fixed;
    top: 0;
  }
}

.drawer-bg {
  background: #000;
  opacity: 0.3;
  width: 100%;
  top: 0;
  height: 100%;
  position: absolute;
  z-index: 999;
}

.fixed-header {
  position: fixed;
  top: 0;
  right: 0;
  z-index: 9;
  // width: calc(100% - #{$sideBarWidth});
  transition: width 0.28s;
}

.hideSidebar .fixed-header {
  width: calc(100% - 54px);
}

.mobile .fixed-header {
  width: 100%;
}
</style>
