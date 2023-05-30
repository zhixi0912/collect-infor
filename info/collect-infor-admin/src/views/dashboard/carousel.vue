<template>
  <div class="">
    <el-carousel :interval="5000">
      <el-carousel-item v-for="item, index in data" :key="index">
        <el-image
          style="width: 100%; height: 100%"
          :src="item.url"
          @click="getImg(item, index)"
          :preview-src-list="previewData"
          :initial-index="index"
          fit="cover"
        />
      </el-carousel-item>
    </el-carousel>
  </div>
</template>

<script lang="ts" setup>
import { onMounted, ref } from 'vue'
import useStore from '@/stores/index'

const imgData = import.meta.glob('@/assets/homeDemo/*')
const { dashboard } = useStore()
const data = ref([])
onMounted(() => {
  previewList()
  dashboard.addImg(previewData)
})
const getImg = (item, index) => {
  console.log('previewData-->', previewData)
}
let previewData = []
const previewList = () => {
  previewData = Object.keys(imgData)
  data.value = previewData.map(item => {
    return { url:item }
  })
}
</script>

<style lang="scss" scoped>

</style>
