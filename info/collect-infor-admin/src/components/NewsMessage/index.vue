<template>
  <div class="right-menu-item hover-effect">
    <el-dropdown
        class="avatar-container right-menu-item hover-effect"
        trigger="click"
      >
        <div class="avatar-wrapper">
          <el-icon class="item-icon">
            <i class="fa fa-bell-o fa-size"></i>
          </el-icon>
        </div>
        <template #dropdown>
          <div class="msg-contnet">
            暂无消息
          </div>
        </template>
      </el-dropdown>
  </div>
</template>

<script lang="ts" setup>

</script>

<style lang="scss" scoped>
.right-menu-item {
  vertical-align: middle;
  .fa-size {
    font-size: 16px;
  }
}
.msg-contnet {
  width: 600px;
  min-height: 50px;
  line-height: 50px;
  text-align: center;
}
.isMsg {
    position: relative;
    .news {
      position: absolute;
      bottom: 1%;
      right: 50%;
      color: #ff0000;
      display: block;
      width: 14px;
      height: 14px;
      border-radius: 50%;
      z-index: 999;
    }
  }
</style>
