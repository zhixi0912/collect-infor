import request from '@/utils/request'

export function getEmployee() {
    return request({
        url: '/api/v1.0/employee',
        method: 'get'
    })
}

export function createEmployee(data) {
    return request({
        url: '/api/v1.0/employee',
        method: 'post',
        data: data
    })
}
export function editEmployee(data) {
    return request({
        url: '/api/v1.0/employee',
        method: 'put',
        data: data
    })
}
export function deleteEmployee(data) {
    return request({
        url: '/api/v1.0/employee',
        method: 'delete',
        data: data
    })
}