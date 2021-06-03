import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../components/Login.vue'
import SignUp from '../components/SignUp.vue'

Vue.use(VueRouter)

const routes = [
  // 配置首页的路由为 Login 组件
  {
    path: '/',
    name: 'Login',
    component: Login
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
]

const router = new VueRouter({
  routes
})

export default router
