<template>
    <div class="info-box">
        <ElCard>
            <template #header>
                <div class="card-header">
                    <span>项目说明</span>
                </div>
            </template>
            <div class="text-box">
                <el-row :gutter="0">
                    <el-col :span="6">
                        <div>
                            <el-image
                                style="width: 100px; height: 100px; cursor: pointer;"
                                :src="img" :fit="fit"
                                :preview-src-list="srcList"
                                :initial-index="1"
                            />
                        </div>
                    </el-col>
                    <el-col :span="18">
                        <div>
                            大雪，是二十四节气中的第21个节气，冬季的第三个节气。斗指壬，太阳到达黄经255度，交节时间为每年公历12月6-8日。大雪节气是干支历子月的起始，标志着仲冬时节正式开始。大雪是反映气候特征的一个节气，大雪节气的特点是气温显著下降、降水量增多。
                        </div>
                    </el-col>
                    <el-col :span="24">
                        “雪”是水汽遇冷的产物，代表寒冷与降水。大雪节气是一个气候概念，它代表的是大雪节气期间的气候特征，即气温与降水量（气象上将雨、雪、雹等从天空下降到地面的水汽凝结物都称为“降水”）。大雪节气与小雪节气一样，都是反映气温与降水变化趋势的节气，它是古代农耕文化对于节令的反映。
                    </el-col>
                </el-row>
            </div>
        </ElCard>
    </div>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue'
import useStore from '@/stores/index'
import img from '@/assets/dog-icon.png'
const fit = 'fill'
const srcList = ref([])
const { dashboard } = useStore()

const getImg = () => {
    srcList.value = dashboard.imgList
}
onMounted(() => {
    setTimeout(()=> {
        getImg()
    }, 500)
})

</script>

<style lang="scss" scoped>
.text-box {
    min-height: 240px;
}
</style>
  