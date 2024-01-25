<template>
  <div class="login-container">
    <el-row :gutter="10">
    <el-col :xs="24" :sm="24" :md="24" :lg="24" :xl="24"
      ><div class="grid-content ep-bg-purple" id="container"
    />
  </el-col>
  </el-row>
    <div class="login-box" v-if="false">
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
import { reactive, ref, toRefs, onMounted } from 'vue'
import type { FormInstance } from 'element-plus'
import { ElNotification } from 'element-plus'
import { login } from '@/api/user'
import storage from '@/utils/storage'
import router from '@/router';
// import Earth from "3d-earth";
import Earth from '@/utils/earth.min.js'

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


function getBgData() {
  var cityList = {
    北京: { name: "北京", longitude: 116.3, latitude: 39.9 },
    上海: { name: "上海", longitude: 121.0, latitude: 31.0 },
    西安: { name: "西安", longitude: 108.0, latitude: 34.0 },
    成都: { name: "成都", longitude: 103.0, latitude: 31.0 },
    乌鲁木齐: { name: "乌鲁木齐", longitude: 87.0, latitude: 43.0 },
    拉萨: { name: "拉萨", longitude: 91.06, latitude: 29.36 },
    广州: { name: "广州", longitude: 113.0, latitude: 23.06 },
    哈尔滨: { name: "哈尔滨", longitude: 127.0, latitude: 45.5 },
    沈阳: { name: "沈阳", longitude: 123.43, latitude: 41.8 },
    武汉: { name: "武汉", longitude: 114.0, latitude: 30.0 },
    海口: { name: "海口", longitude: 110.0, latitude: 20.03 },
    纽约: { name: "纽约", longitude: -74.5, latitude: 40.5 },
    伦敦: { name: "伦敦", longitude: 0.1, latitude: 51.3 },
    巴黎: { name: "巴黎", longitude: 2.2, latitude: 48.5 },
    开普敦: { name: "开普敦", longitude: 18.25, latitude: -33.5 },
    悉尼: { name: "悉尼", longitude: 151.1, latitude: -33.51 },
    东京: { name: "东京", longitude: 139.69, latitude: 35.69 },
    里约热内卢: { name: "里约热内卢", longitude: -43.11, latitude: -22.54 },
  };

  //城市之间的连线，可以定义颜色（数据来自业务系统）
  var bizLines = [
    {
      from: "北京",
      to: [
        "上海",
        "西安",
        "成都",
        "乌鲁木齐",
        "拉萨",
        "广州",
        "哈尔滨",
        "沈阳",
        "武汉",
        "海口",
        "纽约",
        "伦敦",
        "巴黎",
        "开普敦",
        "悉尼",
        "东京",
        "里约热内卢",
      ],
      color: `rgba(255, 147, 0, 1)`,
    },
    {
      from: "上海",
      to: [
        "北京",
        "上海",
        "西安",
        "成都",
        "乌鲁木齐",
        "拉萨",
        "广州",
        "哈尔滨",
        "沈阳",
        "武汉",
        "海口",
        "纽约",
        "伦敦",
        "巴黎",
        "开普敦",
        "悉尼",
        "东京",
        "里约热内卢",
      ],
      color: `rgba(255, 216, 0, 1)`,
    },
    {
      from: "西安",
      to: ["北京", "上海", "成都", "广州", "乌鲁木齐", "海口"],
      color: `rgba(255, 147, 0, 1)`,
    },
    {
      from: "成都",
      to: ["北京", "上海", "广州", "武汉", "海口", "纽约", "悉尼"],
      color: `rgba(255, 147, 0, 1)`,
    },
    {
      from: "乌鲁木齐",
      to: ["北京", "上海", "西安"],
      color: `rgba(255, 147, 0, 1)`,
    },
    {
      from: "广州",
      to: [
        "北京",
        "上海",
        "成都",
        "拉萨",
        "武汉",
        "海口",
        "纽约",
        "伦敦",
        "巴黎",
        "悉尼",
        "东京",
        "里约热内卢",
      ],
      color: `rgba(255, 147, 0, 1)`,
    },
    { from: "哈尔滨", to: ["北京", "沈阳"], color: `rgba(255, 147, 0, 1)` },
    { from: "沈阳", to: ["北京", "哈尔滨"], color: `rgba(255, 147, 0, 1)` },
    {
      from: "海口",
      to: ["北京", "上海", "成都", "广州"],
      color: `rgba(255, 147, 0, 1)`,
    },
    {
      from: "纽约",
      to: ["北京", "上海", "成都", "广州"],
      color: `rgba(255, 147, 0, 1)`,
    },
    {
      from: "伦敦",
      to: ["北京", "上海", "广州"],
      color: `rgba(255, 147, 0, 1)`,
    },
    {
      from: "巴黎",
      to: ["北京", "上海", "广州"],
      color: `rgba(255, 147, 0, 1)`,
    },
    { from: "开普敦", to: ["北京", "上海"], color: `rgba(255, 147, 0, 1)` },
    {
      from: "悉尼",
      to: ["北京", "上海", "成都", "广州"],
      color: `rgba(255, 147, 0, 1)`,
    },
    {
      from: "东京",
      to: ["北京", "上海", "广州"],
      color: `rgba(255, 147, 0, 1)`,
    },
    {
      from: "里约热内卢",
      to: ["北京", "上海", "广州"],
      color: `rgba(255, 147, 0, 1)`,
    },
  ];

    let e = new Earth("container",cityList,bizLines,{autoRotate:true,zoomChina:true,starBackground:true});
    e.load()
}
onMounted(() => {
  // getBgData()

  //城市列表（来自业务系统）
  var cityList = {
          北京: { name: "北京", longitude: 116.3, latitude: 39.9 },
          上海: { name: "上海", longitude: 121.0, latitude: 31.0 },
          西安: { name: "西安", longitude: 108.0, latitude: 34.0 },
          成都: { name: "成都", longitude: 103.0, latitude: 31.0 },
          乌鲁木齐: { name: "乌鲁木齐", longitude: 87.0, latitude: 43.0 },
          拉萨: { name: "拉萨", longitude: 91.06, latitude: 29.36 },
          广州: { name: "广州", longitude: 113.0, latitude: 23.06 },
          哈尔滨: { name: "哈尔滨", longitude: 127.0, latitude: 45.5 },
          沈阳: { name: "沈阳", longitude: 123.43, latitude: 41.8 },
          武汉: { name: "武汉", longitude: 114.0, latitude: 30.0 },
          海口: { name: "海口", longitude: 110.0, latitude: 20.03 },
          纽约: { name: "纽约", longitude: -74.5, latitude: 40.5 },
          伦敦: { name: "伦敦", longitude: 0.1, latitude: 51.3 },
          巴黎: { name: "巴黎", longitude: 2.2, latitude: 48.5 },
          开普敦: { name: "开普敦", longitude: 18.25, latitude: -33.5 },
          悉尼: { name: "悉尼", longitude: 151.1, latitude: -33.51 },
          东京: { name: "东京", longitude: 139.69, latitude: 35.69 },
          里约热内卢: { name: "里约热内卢", longitude: -43.11, latitude: -22.54 },
        };
    
        //城市之间的连线，可以定义颜色（数据来自业务系统）
        var bizLines = [
          {
            from: "北京",
            to: [
              "上海",
              "西安",
              "成都",
              "乌鲁木齐",
              "拉萨",
              "广州",
              "哈尔滨",
              "沈阳",
              "武汉",
              "海口",
              "纽约",
              "伦敦",
              "巴黎",
              "开普敦",
              "悉尼",
              "东京",
              "里约热内卢",
            ],
            color: `rgba(255, 147, 0, 1)`,
          },
          {
            from: "上海",
            to: [
              "北京",
              "上海",
              "西安",
              "成都",
              "乌鲁木齐",
              "拉萨",
              "广州",
              "哈尔滨",
              "沈阳",
              "武汉",
              "海口",
              "纽约",
              "伦敦",
              "巴黎",
              "开普敦",
              "悉尼",
              "东京",
              "里约热内卢",
            ],
            color: `rgba(255, 216, 0, 1)`,
          },
          {
            from: "西安",
            to: ["北京", "上海", "成都", "广州", "乌鲁木齐", "海口"],
            color: `rgba(255, 147, 0, 1)`,
          },
          {
            from: "成都",
            to: ["北京", "上海", "广州", "武汉", "海口", "纽约", "悉尼"],
            color: `rgba(255, 147, 0, 1)`,
          },
          {
            from: "乌鲁木齐",
            to: ["北京", "上海", "西安"],
            color: `rgba(255, 147, 0, 1)`,
          },
          {
            from: "广州",
            to: [
              "北京",
              "上海",
              "成都",
              "拉萨",
              "武汉",
              "海口",
              "纽约",
              "伦敦",
              "巴黎",
              "悉尼",
              "东京",
              "里约热内卢",
            ],
            color: `rgba(255, 147, 0, 1)`,
          },
          { from: "哈尔滨", to: ["北京", "沈阳"], color: `rgba(255, 147, 0, 1)` },
          { from: "沈阳", to: ["北京", "哈尔滨"], color: `rgba(255, 147, 0, 1)` },
          {
            from: "海口",
            to: ["北京", "上海", "成都", "广州"],
            color: `rgba(255, 147, 0, 1)`,
          },
          {
            from: "纽约",
            to: ["北京", "上海", "成都", "广州"],
            color: `rgba(255, 147, 0, 1)`,
          },
          {
            from: "伦敦",
            to: ["北京", "上海", "广州"],
            color: `rgba(255, 147, 0, 1)`,
          },
          {
            from: "巴黎",
            to: ["北京", "上海", "广州"],
            color: `rgba(255, 147, 0, 1)`,
          },
          { from: "开普敦", to: ["北京", "上海"], color: `rgba(255, 147, 0, 1)` },
          {
            from: "悉尼",
            to: ["北京", "上海", "成都", "广州"],
            color: `rgba(255, 147, 0, 1)`,
          },
          {
            from: "东京",
            to: ["北京", "上海", "广州"],
            color: `rgba(255, 147, 0, 1)`,
          },
          {
            from: "里约热内卢",
            to: ["北京", "上海", "广州"],
            color: `rgba(255, 147, 0, 1)`,
          },
        ];
    
          let e = new Earth("container",cityList,bizLines,{autoRotate:true,zoomChina:true,starBackground:true});
          e.load()
})
</script>

<style lang="scss" scoped>
.grid-content{
  width: 100vw;
  height: 100vh;
  background: black;
}
.login-container {
  /* background-color: bisque; */
  // background-image: url('@/assets/login-bg1.jpg');
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
