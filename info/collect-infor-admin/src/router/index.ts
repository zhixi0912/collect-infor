import { createRouter, createWebHashHistory } from 'vue-router'
import { ElNotification } from 'element-plus'
import storage from '@/utils/storage'
export const Layout = () => import('@/views/layout/index.vue');

const router = createRouter({
  history: createWebHashHistory(),
  routes: [
    {
      path: '/login',
      name: 'login',
      meta: { hidden: true },
      component: () => import('@/views/login/index.vue')
    },
    {
      path: '/:pathMatch(.*)',
      redirect: '/404',
      meta: { hidden: true }
    },
    {
      path: '/',
      component: Layout,
      redirect: '/dashboard',
      children: [
        {
          path: 'dashboard',
          component: () => import('@/views/dashboard/index.vue'),
          name: 'Dashboard',
          meta: { title: '仪表盘', icon: 'fa fa-home fa-2' }
        },
        {
          path: '/404',
          name: '404',
          component: () => import('@/views/error-page/404.vue'),
          meta: { hidden: true },
        }
      ]
    },
    {
      path: '/system',
      component: Layout,
      redirect: '/system/user',
      meta: { title: '系统管理', icon: 'fa fa-desktop', affix: true, alwaysShow: true },
      children: [
        {
          path: 'user',
          component: () => import('@/views/system/user/index.vue'),
          name: 'user',
          meta: { title: '用户管理', icon: 'fa fa-user-o', alwaysShow: false }
        },
        {
          path: 'role',
          component: () => import('@/views/system/role/index.vue'),
          name: 'role',
          meta: { title: '角色管理', icon: 'fa fa-address-book-o', alwaysShow: false }
        },
      ]
    },
    {
      path: '/test',
      component: Layout,
      redirect: '/test/test2',
      meta: { title: '测试一级', icon: 'fa fa-desktop', affix: true, alwaysShow: true },
      children: [
        {
          path: 'test2',
          name: 'test2',
          meta: { title: '测试二级', icon: 'fa fa-user-o', affix: true, alwaysShow: true },
          redirect: '/test/test2/test3',
          children: [
            {
              path: 'test3',
              component: () => import('@/views/test/test2/index.vue'),
              name: 'test3',
              meta: { title: '测试三级', icon: 'fa fa-user-o', alwaysShow: false }
            }
          ]
        }
      ]
    }
  ],
  // 刷新时，滚动条位置还原
  scrollBehavior: () => ({ left: 0, top: 0 })
})

router.beforeEach((to, from, next) => {
  const token = storage.ss.get("token")
  if (token) {
    next()
  } else {
    if (to.path == '/login') {
      next()
    } else {
      ElNotification({
        title: '错误',
        message: '请重新登录！',
        type: 'error'
      })
      next({path: 'login'})
    }
  }
})

export default router
