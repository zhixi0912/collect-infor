<template>
  <el-drawer
    v-model="isShow"
    :direction="direction"
    :before-close="handleClose"
    :destroy-on-close="true"
    size="800px"
    custom-class="drawer-box"
  >
    <template #header>
      <span>{{ props.employeeRow.employee_id ? '修改' : '新增'}}员工信息</span>
    </template>
    <template #default>
      <div>
        <el-form
          ref="formDataRef"
          :model="formData"
          :rules="rules"
          label-width="120px"
          class="demo-formData"
          :size="formSize"
          status-icon
        >
        <el-row>
          <el-col :span="12">
            <el-form-item label="姓名" prop="employee_name">
              <el-input v-model="formData.employee_name" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="性别" prop="employee_gend">
              <el-select v-model="formData.employee_gend" placeholder="性别" class="item-box">
                <el-option :label="item.option" :value="item.value" v-for="item, index in gendData" :key="index" />
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="民族" prop="employee_nation">
              <el-input v-model="formData.employee_nation" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="电话" prop="employee_phone">
              <el-input v-model="formData.employee_phone" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="出生日期" prop="employee_birthday">
              <el-date-picker
              v-model="formData.employee_birthday"
              placeholder="选择出生日期"
              format="YYYY-MM-DD"
              value-format="YYYY-MM-DD"
              style="width: 100%"
            />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="身份证号" prop="employee_id_card">
              <el-input v-model="formData.employee_id_card" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="银行卡号" prop="employee_bank_card">
              <el-input v-model="formData.employee_bank_card" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="所属银行" prop="employee_bank">
              <el-input v-model="formData.employee_bank" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="身份证地址" prop="employee_address">
              <el-input v-model="formData.employee_address" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="职业" prop="employee_occupation">
              <el-input v-model="formData.employee_occupation" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="职务" prop="employee_post">
              <el-input v-model="formData.employee_post" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="其他" prop="employee_content">
              <el-input v-model="formData.employee_content" />
            </el-form-item>
          </el-col>
          <el-col :span="12"></el-col>
          <el-col :span="12"></el-col>
        </el-row>
          
        </el-form>
      </div>
    </template>
    <template #footer>
      <div style="flex: auto; text-align: center;">
        <el-button @click="cancel(formDataRef)">取消</el-button>
        <el-button type="primary" @click="submitForm(formDataRef, emit)">提交</el-button>
      </div>
    </template>
  </el-drawer>
</template>

<script lang="ts" setup>
import { ref, reactive, toRefs, onBeforeMount } from 'vue'
import type { FormInstance, FormRules } from 'element-plus'
import addInfo from './addInfo'

const props = defineProps({
  employeeRow: {
    type: Object,
    default: {}
  }
})
const emit = defineEmits(['confirmForm'])

const isClose = () => {
  isShow.value = false
}

const {
  formData,
  gendData,
  rules,
  isShow,
  formSize,
  submitForm
} = addInfo()
const formDataRef = ref<FormInstance>()

const isOpen = (row) => {
  formData.value = row
  isShow.value = true
}
/*
vue3中规定，使用了 <script setup> 的组件是默认私有的：
一个父组件无法访问到一个使用了 <script setup> 的子组件中的任何东西，
除非子组件在其中通过 defineExpose 宏显式暴露
*/
defineExpose({
  isOpen,
  isClose
})
const direction = ref('rtl')

const cancel = (formEl: FormInstance | undefined) => {
  if (!formEl) return
  formEl.resetFields()
  isClose()
}
const handleClose = (done: () => void) => {
  isClose()
}
</script>

<style lang="scss" scoped>
.item-box {
  width: 100%;
}
</style>
