<template>
  <div class="">
    <div id="main" class="echarts-box"></div>
  </div>
</template>

<script lang="ts" setup>
import { onMounted } from 'vue'
// 引入 echarts 核心模块，核心模块提供了 echarts 使用必须要的接口。
import * as echarts from 'echarts/core';
// 引入柱状图图表，图表后缀都为 Chart
import { BarChart } from 'echarts/charts';
// 引入提示框，标题，直角坐标系，数据集，内置数据转换器组件，组件后缀都为 Component
import {
  TitleComponent,
  TooltipComponent,
  GridComponent,
  DatasetComponent,
  TransformComponent
} from 'echarts/components';
// 标签自动布局，全局过渡动画等特性
import { LabelLayout, UniversalTransition } from 'echarts/features';
// 引入 Canvas 渲染器，注意引入 CanvasRenderer 或者 SVGRenderer 是必须的一步
import { CanvasRenderer } from 'echarts/renderers';
import { ToolboxComponent } from 'echarts/components';
import { LegendComponent } from 'echarts/components';
import { LineChart } from 'echarts/charts';
echarts.use([ToolboxComponent]);
echarts.use([LegendComponent]);
echarts.use([LineChart]);
// 注册必须的组件
echarts.use([
  TitleComponent,
  TooltipComponent,
  GridComponent,
  DatasetComponent,
  TransformComponent,
  BarChart,
  LabelLayout,
  UniversalTransition,
  CanvasRenderer
]);

onMounted(() => {
  // 接下来的使用就跟之前一样，初始化图表，设置配置项
    
  var chartDom = document.getElementById('main');
  var myChart = echarts.init(chartDom);
  var option;

  option = {
    title: { text: '上海一周气温降水图', left: '30%', top: '0' },
    tooltip: {
      trigger: 'axis',
      axisPointer: {
        type: 'cross',
        crossStyle: {
          color: '#999'
        }
      }
    },
    legend: {
      top: '30',
      data: ['蒸发', '降水', '温度']
    },
    grid: {
      bottom: '20',
      left: '12%'
    },
    xAxis: [
      {
        type: 'category',
        data: ['周一', '周二', '周三', '周四', '周五', '周六', '周日'],
        axisPointer: {
          type: 'shadow'
        }
      }
    ],
    yAxis: [
      {
        type: 'value',
        name: '降水',
        min: 0,
        max: 250,
        interval: 50,
        axisLabel: {
          formatter: '{value} ml'
        }
      },
      {
        type: 'value',
        name: '温度',
        min: 0,
        max: 25,
        interval: 5,
        axisLabel: {
          formatter: '{value} °C'
        }
      }
    ],
    series: [
      {
        name: '蒸发',
        type: 'bar',
        tooltip: {
          valueFormatter: function (value) {
            return value + ' ml';
          }
        },
        data: [
          2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3
        ]
      },
      {
        name: '降水',
        type: 'bar',
        tooltip: {
          valueFormatter: function (value) {
            return value + ' ml';
          }
        },
        data: [
          2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3
        ]
      },
      {
        name: '温度',
        type: 'line',
        yAxisIndex: 1,
        tooltip: {
          valueFormatter: function (value) {
            return value + ' °C';
          }
        },
        data: [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2]
      }
    ]
  };

option && myChart.setOption(option);
})

</script>

<style lang="scss" scoped>
.echarts-box {
  height: 300px;
}
</style>
