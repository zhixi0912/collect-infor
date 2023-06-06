<template>
  <div class="app-container">
    <div class="search">
        <el-form
          :inline="true"
          :model="formInline"
          :rules="rules"
          ref="ruleFormRef"
          class="demo-form-inline"
        >
          <el-form-item label="关键字" prop="employee_name">
            <el-input v-model="formInline.employee_name" placeholder="请输入姓名" />
          </el-form-item>
          <el-form-item prop="employee_id_card">
            <el-input v-model.number="formInline.employee_id_card" placeholder="请输入身份证号" />
          </el-form-item>
          <el-form-item prop="employee_bank_card">
            <el-input v-model.number="formInline.employee_bank_card" placeholder="请输入银行卡号" />
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="onSearch(ruleFormRef)"> <i class="fa fa-search el-icon--left"></i>查询</el-button>
            <el-button @click="onReset(ruleFormRef)"> <i class="fa fa-refresh el-icon--left"></i>重置</el-button>
          </el-form-item>
        </el-form>
    </div>
    <ElCard>
      <template #header>
        <div class="card-header">
          <el-button type="success" @click="addEmployee"><i class="fa fa-plus el-icon--left"></i>新增</el-button>
          <el-button type="danger" :disabled="multipleSelection.length > 0 ? false : true"><i class="fa fa-trash el-icon--left"></i>删除</el-button>
        </div>
      </template>
      <el-table
        ref="multipleTableRef"
        :data="tableData"
        stripe
        border
        style="width: 100%"
        @selection-change="handleSelectionChange"
      >
        <el-table-column type="selection" width="55" fixed />
        <el-table-column property="employee_name" fixed label="姓名" width="80" />
        <el-table-column property="employee_gend" label="性别" width="80" />
        <el-table-column property="employee_phone" label="电话" width="120" />
        <el-table-column property="employee_birthday" label="出生日期" width="120" />
        <el-table-column property="employee_id_card" label="身份证号" width="220"/>
        <el-table-column property="employee_address" label="地址" width="360" />
        <el-table-column property="employee_nation" label="民族" width="80" />
        <el-table-column property="employee_occupation" label="职业" width="120" />
        <el-table-column property="employee_post" label="职务" width="120" />
        <el-table-column property="employee_bank_card" label="银行卡号" width="220" />
        <el-table-column property="employee_bank" label="所属银行" width="120" />
        <el-table-column property="employee_content" label="其他" width="300" />
        <el-table-column label="操作" fixed="right" width="160">
          <template #default="scope">
            <el-button size="small" @click="handleEdit(scope.$index, scope.row)"
              >修改</el-button
            >
            <el-button
              size="small"
              type="danger"
              @click="handleDelete(scope.$index, scope.row)"
              >删除</el-button
            >
          </template>
        </el-table-column>
      </el-table>
    </ElCard>
  </div>
  <AddOrEditDrawer ref="drawer" :employeeRow="employeeRow" @confirmForm="subData" />
</template>

<script lang="ts" setup>
import { reactive, ref, onMounted } from 'vue'
import { ElTable, ElMessageBox } from 'element-plus'
import type { FormInstance } from 'element-plus'
import { getEmployee, deleteEmployee } from '@/api/employee'
import AddOrEditDrawer from './addOrEditDrawer.vue'

const formInline = reactive({
  employee_name: '',
  employee_id_card: '',
  employee_bank_card: ''
})
const ruleFormRef = ref<FormInstance>()
const multipleTableRef = ref()
const multipleSelection = ref([])
const tableData = ref([])
const drawer = ref<InstanceType<typeof AddOrEditDrawer> | null>(null)
const employeeRow = ref<object>([])
const rules = reactive({
  employee_id_card: [
    {
      type: 'number',
      message: 'Please input number',
    }
  ],
  employee_bank_card: [
    {
      type: 'number',
      message: 'Please input number',
    }
  ]
})
onMounted(() => {
  feach()
})
const feach =() => {
  getEmployee().then(res => {
    tableData.value = res.data
  })
}
const onSearch = (formEl) => {
  if (!formEl) return
  formEl.validate((valid) => {
    if (valid) {
      console.log('submit!')
    } else {
      return false
    }
  })
  console.log('submit!', formEl)
}
const onReset = (formEl: FormInstance | undefined) => {
  if (!formEl) return
  formEl.resetFields()
}

const handleSelectionChange = (val) => {
  console.log('val-->', val)
  multipleSelection.value = val
}
const addEmployee = () => {
  employeeRow.value = {}
  drawer.value?.isOpen({})
}
const handleEdit = (index, row) =>{
  employeeRow.value = row
  drawer.value?.isOpen(row)
}
const handleDelete = (index, row) =>{
  ElMessageBox.confirm(
    '确定要删除这条信息吗?',
    '警告',
    {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning',
    }
  ).then(() => {
    deleteFeach(row)
  })
}
const deleteFeach =(data) => {
  deleteEmployee(data).then(res => {
    feach()
  })
}
const subData = (val) => {
  drawer.value?.isClose()
  feach()
}
</script>

<style lang="scss" scoped>
</style>
