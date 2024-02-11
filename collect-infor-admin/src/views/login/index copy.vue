<template>
  <div class="login-container">
    <div class="login-box">
      <el-card class="box-card">
        <template #header>
          <div class="card-header">
            <!-- <div class="logo-box">
              <img :src="logo" class="login-logo" />
            </div> -->
            <span>后台管理系统</span>
          </div>
        </template>
        <div class="login-form">
          <el-form
            ref="ruleFormRef"
            :model="ruleForm"
            status-icon
            :rules="rules"
            class="demo-ruleForm"
          >
            <el-form-item prop="userName">
              <el-input v-model="ruleForm.userName" autocomplete="off" placeholder="请输入用户名">
                <template #prefix>
                  <el-icon class="el-input__icon">
                    <i class="fa fa-user"></i>
                  </el-icon>
                </template>
              </el-input>
            </el-form-item>
            <el-form-item prop="userPassword">
              <el-input
                v-model="ruleForm.userPassword"
                type="password"
                autocomplete="off"
                placeholder="请输入密码"
              >
                <template #prefix>
                  <el-icon class="el-input__icon">
                    <i class="fa fa-lock"></i>
                  </el-icon>
                </template>
              </el-input>
            </el-form-item>
            <!-- <el-form-item prop="userVerifycode">
              <el-input v-model="ruleForm.userVerifycode">
                <template #prefix>
                  <el-icon class="el-input__icon">
                    <i class="fa fa-barcode"></i>
                  </el-icon>
                </template>
                <template #append>
                  <el-tooltip
                    class="box-item"
                    effect="light"
                    content="点击刷新验证码"
                    placement="top-start"
                  >
                    <el-button>
                      <el-icon class="el-input__icon">
                        <i class="fa fa-address-card"></i>
                      </el-icon>
                    </el-button>
                  </el-tooltip>
                </template>
              </el-input>
            </el-form-item> -->
            <el-form-item>
              <el-button type="primary" class="sub-btn" @click="submitForm(ruleFormRef)"
                >登录</el-button
              >
            </el-form-item>
          </el-form>
        </div>
      </el-card>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { reactive, ref, toRefs } from 'vue'
import type { FormInstance } from 'element-plus'
import { ElNotification } from 'element-plus'
import storage from '@/utils/storage'
import router from '@/router';
import { login } from '@/api/user'

// const state = reactive({
//   logo: new URL(`../../assets/logo.svg`, import.meta.url).href
// })
// const { logo } = toRefs(state);
const ruleFormRef = ref<FormInstance>()
const ruleForm = reactive({
  userName: '',
  userPassword: '',
  userVerifycode: '',
})

const validateName = (rule: any, value: any, callback: any) => {
  if (value === '') {
    callback(new Error('请输入用户名！'))
  } else {
    callback()
  }
}
const validatePass = (rule: any, value: any, callback: any) => {
  if (value === '') {
    callback(new Error('请输入密码！'))
  } else {
    callback()
  }
}

const validateCode = (rule: any, value: any, callback: any) => {
  if (value === '') {
    callback(new Error('请输入验证码！'))
    console.log('value-------->', value,value)
  } else {
    callback()
  }
}

const rules = reactive({
  userName: [{ validator: validateName, trigger: 'blur' }],
  userPassword: [{ validator: validatePass, trigger: 'blur' }],
  userVerifycode: [{ validator: validateCode, trigger: 'blur' }]
})

const submitForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return
  formEl.validate((valid) => {
    if (valid) {
      const data = {
        username: ruleForm.userName,
        password: ruleForm.userPassword
      }
      login(data)
      .then(res => {
        if (res.data) {
          storage.ss.set('token', res.data.token)
          msgOpen('登录成功！', 'success')
          router.push({
            path: '/dashboard'
          })
        } else {
          msgOpen('登录失败', 'error')
        }
      })
      .catch(err =>{
        msgOpen(err.msg, 'error')
      })
    } else {
      console.log('用户名或密码错误！')
      return false
    }
  })
}

const msgOpen = (msg, msgType) => {
  ElNotification({
    // title: msgType,
    message: msg,
    type: msgType
  })
}
</script>

<style lang="scss" scoped>
.login-container {
  /* background-color: bisque; */
  background-image: url('@/assets/login-bg1.jpg');
  background-position: 0 center;
  background-repeat: no-repeat;
  background-size: cover;
  min-height: 100%;
  width: 100%;
  overflow: hidden;
  .login-box {
    width: 400px;
    margin: 0 auto;
    margin-top: calc(100vh / 2 - 150px);
    .card-header {
      text-align: center;
      font-size: 38px;
      position: relative;
      .logo-box {
        position: absolute;
        left: 50%;
        top: -50px;
        .login-logo {
          width: 60px;
          height: 60px;
        }
      }
    }
    .login-form {
      padding: 0 30px;
      .sub-btn {
        width: 100%;
      }
    }
  }
}
</style>
