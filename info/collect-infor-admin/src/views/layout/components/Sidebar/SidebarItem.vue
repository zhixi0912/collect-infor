<template>
  <div v-if="!item.meta || !item.meta.hidden">
    <template
      v-if="
        hasOneShowingChild(item.children, item) &&
        (!onlyOneChild.children || onlyOneChild.noShowingChildren) &&
        (!item.meta || !item.meta.alwaysShow)
      "
    >
    <router-link :to="resolvePath(onlyOneChild.path)">
        <el-menu-item v-if="onlyOneChild.meta" :index="resolvePath(onlyOneChild.path)" :class="{ 'submenu-title-noDropdown': !isNest }">
          <el-icon><i :class="onlyOneChild.meta.icon"></i></el-icon>
          <template #title>{{ onlyOneChild.meta.title }}</template>
        </el-menu-item>
      </router-link>
    </template>
    <el-sub-menu v-else :index="resolvePath(item.path)" popper-append-to-body>
      <template #title>
        <el-icon><i :class="item.meta.icon"></i></el-icon>
        <span>{{ item.meta.title }}</span>
      </template>
      <SidebarItem
        v-for="child in item.children"
        :key="child.path"
        :item="child"
        :is-nest="true"
        :base-path="resolvePath(child.path)"
        class="nest-menu"
      />
    </el-sub-menu>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import path from 'path-browserify'
const props = defineProps({
  item: {
    type: Object,
    required: true
  },
  isNest: {
    type: Boolean,
    required: false
  },
  basePath: {
    type: String,
    required: true
  }
});
const onlyOneChild = ref();
function hasOneShowingChild(children, parent) {
  if (!children) {
    children = []
  }
  const showingChildren = children.filter((item: any) => {
    if (item.meta && item.meta.hidden) {
      return false;
    } else {
      onlyOneChild.value = item;
      return true;
    }
  });
  if (showingChildren.length === 1) {
    return true;
  }

  if (showingChildren.length === 0) {
    onlyOneChild.value = { ...parent, path: '', noShowingChildren: true };
    return true;
  }

  return false;
}

function resolvePath(routePath: string) {
  return path.resolve(props.basePath, routePath);
}

</script>

<style lang="scss" scoped></style>
