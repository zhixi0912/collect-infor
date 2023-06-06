<template>
  <div class="has-logo" :data-a="isCollapse">
    <Logo />
    <el-scrollbar>
      <el-menu
      :default-active="activeMenu"
      :collapse="isCollapse"
      :background-color="variables.menuBg"
      :text-color="variables.menuText"
      :active-text-color="variables.menuActiveText"
      :unique-opened="false"
      :collapse-transition="false"
      mode="vertical"
      >
        <SidebarItem
          v-for="item in router.options.routes"
          :item="item"
          :key="item.path"
          :base-path="item.path"
          :is-collapse="isCollapse"
        />
      </el-menu>
    </el-scrollbar>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import SidebarItem from './SidebarItem.vue';
import variables from '@/styles/variables.module.scss';
import Logo from './Logo.vue';
import useStore from '@/stores/index'

const route = useRoute();
const router = useRouter()
const { sidebar } = useStore()
const isCollapse = computed(() => sidebar.isCollapse);
const activeMenu = computed(() => {
  const { meta, path } = route;
  if (meta.activeMenu) {
    return meta.activeMenu as string;
  }
  return path;
});
</script>