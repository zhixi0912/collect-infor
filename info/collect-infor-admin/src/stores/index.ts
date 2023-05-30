import { defineStore } from 'pinia'

const dashboardStore = defineStore('imgStore', {
    state() {
        return {
            imgList: []
        }
    },
    actions: {
        addImg(data){
            this.imgList = [...data]
        }
    }
})

const navActive = defineStore('isCollapse', {
    state() {
        return {
            isCollapse: false
        }
    },
    actions: {
        switchStatus() {
            this.isCollapse = !this.isCollapse
        }
    }
})

const useStore = () => ({
    dashboard: dashboardStore(),
    sidebar: navActive()
})
export default useStore