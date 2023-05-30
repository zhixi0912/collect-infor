<template>
  <div class="dashboard-container">
    <el-row :gutter="20" class="dashboard-box">
      <el-col :span="6" v-for="item, index in h1Data" :key="index">
        <ElCard>
          <div class="h1-box clearfix">
            <div class="icon-box" :class="'cl-box-' + (index + 1)">
              <i class="fa" :class="item.inco"></i>
            </div>
            <div class="text-box">
              <div>{{ item.name }}</div>
              <div>{{ item.value }}</div>
            </div>
          </div>
        </ElCard>
      </el-col>
    </el-row>
    <el-row :gutter="20" class="dashboard-box">
      <el-col :span="8">
        <ElCard>
          <MixedLineAndBar />
        </ElCard>
      </el-col>
      <el-col :span="8">
        <ElCard>
          <CityMap />
        </ElCard>
      </el-col>
      <el-col :span="8">
        <ElCard>
          <NationalMap />
        </ElCard>
      </el-col>
    </el-row>

    <el-row :gutter="20" class="dashboard-box">
      <el-col :span="12">
        <ProjectInfo />
      </el-col>
      <el-col :span="12">
        <ElCard><Carousel /></ElCard>
      </el-col>
    </el-row>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import { mathSum } from '@/utils/index'
import MixedLineAndBar from './mixedLineAndBar.vue'
import CityMap from './cityMap.vue'
import NationalMap from './nationalMap.vue'
import Carousel from './carousel.vue'
import ProjectInfo from './projectInfo.vue'

const h1Data = ref([
  {
    name: "员工数",
    inco: 'fa-user',
    value: mathSum(20, 30)
  },
  {
    name: "出勤数",
    inco: 'fa-address-book-o',
    value: mathSum(15, 20)
  },
  {
    name: "消息数",
    inco: 'fa-envelope-o',
    value: mathSum(0, 30)
  },
  {
    name: "订单数",
    inco: 'fa-truck',
    value: mathSum(10, 300)
  }
])
</script>

<style lang="scss" scoped>
.dashboard-container {
  padding: 24px;
  background-color: #f0f2f5;
  position: relative;
  .dashboard-box {
    margin-bottom: 10px;
    .h1-box {
      .icon-box {
        float: left;
        height: 52px;
        width: 60px;
        text-align: center;
        border-radius: 5px;
        i {
          font-size: 3rem;
          color: #f3d8ba;
          vertical-align: middle;
        }
        &:hover {
          width: 60px;
          text-align: center;
          background-color: #f3d8ba;
          i {
            vertical-align: middle;
            color: #ffffff;
          }
        }
      }
      .cl-box-1{
        i {
          color: #f3d8ba;
        }
        &:hover {
          background-color: #f3d8ba;
        }

      }
      .cl-box-2{
        i {
          color: #c3ceb0;
        }
        &:hover {
          background-color: #c3ceb0;
          padding-top: 3px;
          i {
            font-size: 2.8rem;
          }
        }
      }
      .cl-box-3{
        i {
          color: #c6aa9f;
        }
        &:hover {
          background-color: #c6aa9f;
        }
      }
      .cl-box-4{
        i {
          color: #9d6f5f;
        }
        &:hover {
          background-color: #9d6f5f;
        }
      }
      .text-box {
        float: right;
        text-align: right;
        div:first-child {
          margin-bottom: 5px;
        }
        div:last-child {
          text-align: right;
          font-weight: bold;
        }
      }
    }
  }
  .dashboard-box:last-child{
      margin-bottom: 0;
    }
}
</style>
