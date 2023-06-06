import { reactive, toRefs } from "vue"
import type { FormInstance, FormRules } from 'element-plus'
import { ElNotification } from 'element-plus'
import { createEmployee, editEmployee } from '@/api/employee'

const addInfo = () => {
    const state = reactive({
        formData: {
            employee_id: '',
            employee_name: '',
            employee_gend: '',
            employee_nation: '',
            employee_phone: '',
            employee_birthday: '',
            employee_id_card: '',
            employee_bank_card: '',
            employee_bank: '',
            employee_address: '',
            employee_occupation: '',
            employee_post: '',
            employee_content: ''
        },
        rules: {
            employee_name: [
              { required: true, message: '请填写姓名', trigger: 'change' },
              { min: 2, max: 20, message: '姓名太长或太短', trigger: 'blur' },
            ],
            employee_gend: [
              {
                required: true,
                message: '请选择性别',
                trigger: 'change',
              },
            ],
            employee_nation: [
              {
                required: true,
                message: '请填写民族',
                trigger: 'change',
              },
            ],
            employee_phone: [
              {
                required: true,
                message: '请填写电话',
                trigger: 'change',
              },
              {
                pattern: /^1[3|4|5|6|7|8|9][0-9]\d{8}$/,
                message: "请输入正确的手机号码",
                trigger: "blur"
              }
            ],
            employee_birthday: [
              {
                required: true,
                message: '请选择出生日期',
                trigger: 'change',
              },
            ],
            employee_id_card: [
              {
                required: true,
                message: '请填写身份证号码',
                trigger: 'change',
              },
              {
                pattern:/(^\d{15}$)|(^\d{18}$)|(^\d{17}(\d|X|x)$)/,
                message: '请填写正确的身份证号码',
                trigger: 'blur',
              }
            ],
            employee_bank_card: [
              {
                required: true,
                message: '请填写银行卡号码',
                trigger: 'change',
              },
            ],
            employee_bank: [
              {
                required: true,
                message: '请填写所属银行',
                trigger: 'change',
              },
            ],
            employee_address: [
              {
                required: true,
                message: '请填写身份证地址',
                trigger: 'change',
              },
            ],
            employee_occupation: [
              {
                required: true,
                message: '请填写职业',
                trigger: 'change',
              },
            ],
            employee_post: [
              {
                required: true,
                message: '请填写职务',
                trigger: 'change'
              }
            ],
            employee_content: [
                {
                    required: true,
                    message: '请填写职务',
                    trigger: 'change'
                }
            ],
        },
        gendData: [
            {
              option: '男',
              value: '男'
            },
            {
              option: '女',
              value: '女'
            },
            {
              option: '保密',
              value: '保密'
            }
        ],
        isShow: false,
        formSize: 'default'
    })
    const {
        formData,
        gendData,
        rules,
        isShow,
        formSize
    } = toRefs(state)
    
    const submitForm = async (formEl: FormInstance | undefined, emit) => {
        if (!formEl) return
        await formEl.validate((valid, fields) => {
          if (valid) {
            if (formData.value.employee_id) {
                editFetch(formData.value, emit)
            } else {
                createFetch(formData.value, emit)
            }
          } else {
            console.log('error submit!', fields)
          }
        })
    }
    const createFetch = (data, emit) => {
        createEmployee(data).then(res => {
            msgOpen('创建成功！')
            emit('confirmForm', 'OK')
        })
    }
    const editFetch = (data, emit) => {
        editEmployee(data).then(res => {
            msgOpen('修改成功！')
            emit('confirmForm', 'OK')
        })
    }
    const msgOpen = (msg) => {
        ElNotification({
          message: msg,
          type: 'success'
        })
      }
    return {
        formData,
        gendData,
        rules,
        isShow,
        formSize,
        submitForm
    }
}

export default addInfo