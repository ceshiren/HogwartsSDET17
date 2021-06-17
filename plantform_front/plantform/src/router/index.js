import Vue from "vue";
import VueRouter from "vue-router";
import Login from "../components/Login.vue";
import Main from "../components/Main.vue";
import SignUp from "../components/SignUp.vue";
import TestReport from "../components/TestReport.vue";
import TestCase from "../components/TestCase.vue";

Vue.use(VueRouter);

const routes = [
  // 配置首页的路由为 Login 组件
  {
    path: "/",
    name: "Login",
    component: Login,
  },
  {
    path: "/sign-up",
    name: "SignUp",
    component: SignUp,
  },
  // children 代表子路由，子路由加载前，会加载其父路由
  {
    path: "/main",
    name: "Main",
    component: Main,
    children: [
      {
        path: "/report",
        name: "TestReport",
        component: TestReport,
      },
      {
        path: "/testcase",
        name: "TestCase",
        component: TestCase,
      },
    ],
  },
];

const router = new VueRouter({
  routes,
});

export default router;
