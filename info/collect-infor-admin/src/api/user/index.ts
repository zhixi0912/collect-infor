import request from '@/utils/request'

export function login(data: any) {
    return request({
        url: '/api/v1.0/login',
        method: 'post',
        data: data
    })
}

export function loginOut() {
    return request({
        url: '/api/v1.0/login_out',
        method: 'delete'
    })
}