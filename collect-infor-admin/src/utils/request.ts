import axios from "axios";
import storage from '@/utils/storage'

const service = axios.create({
    baseURL: import.meta.env.VITE_APP_BASE_API,
    // baseURL: 'http://43.139.138.4:9500',
    timeout: 5000,
    headers: { 'Content-Type': 'application/json;charset=utf-8' }
})

service.interceptors.request.use(config => {
    const token = storage.ss.get("token")
    if (token) {
        config.headers.Authorization = "Bearer " +token
    }
    return config
},error => {
    console.log(error)
    return Promise.reject(error)
})

service.interceptors.response.use(response => {
    // console.log('response-->', response)
    return response.data
},error =>{
    console.log('403', error)
    return Promise.reject(error)
})

export default service