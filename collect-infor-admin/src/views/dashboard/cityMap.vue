<template>
  <div class="">
    <div id="main" ref="chart" class="echarts-box"></div>
  </div>
</template>

<script lang="ts" setup>
import { onMounted, ref } from 'vue'
import { mathSum } from '@/utils/index'
// 引入 echarts 核心模块，核心模块提供了 echarts 使用必须要的接口。
import * as echarts from 'echarts/core';
import {
  TitleComponent,
  ToolboxComponent,
  TooltipComponent,
  VisualMapComponent,
  GeoComponent
} from 'echarts/components';
import { MapChart } from 'echarts/charts';
import { CanvasRenderer } from 'echarts/renderers';
import sh from '@/assets/mapdata/shanghai.json'

echarts.use([
  TitleComponent,
  ToolboxComponent,
  TooltipComponent,
  VisualMapComponent,
  GeoComponent,
  MapChart,
  CanvasRenderer
]);
const chart = ref()
onMounted(() => {
  init(sh)
})
// const getData = async () => {
//   var ROOT_PATH = 'https://geo.datav.aliyun.com';
//   await axios.get(ROOT_PATH + '/areas_v3/bound/310000_full.json').then(res => {
//     // console.log('res-->', res.data)
//     init(res.data)
//   }).catch(err => {

//   });
// }

const init = (data) => {
  let result = data.features.map(item => {
    let val = mathSum(800, 50000)
    return {
      name: item.properties.name,
      value: val
    }
  })
  var myChart = echarts.init(chart.value)
  echarts.registerMap('sh', data)
  var option = {
    title: {
      text: '上海疫情感染分布图'
    },
    visualMap: {
        min: 800,
        max: 50000,
        text: ['高', '低'],
        realtime: false,
        calculable: true,
        inRange: {
          color: ['lightskyblue', 'yellow', 'orangered']
        }
      },
    series: [
      {
        type: 'map',
        map: 'sh',
        data: result
      }
    ]
  }
  myChart.setOption(option)
}
</script>

<style lang="scss" scoped>
.echarts-box {
  height: 300px;
}
</style>
