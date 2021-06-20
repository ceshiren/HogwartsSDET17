import axios from "axios";
import router from "../router/index.js";
// 创建 axios 的实例
const instance = axios.create({
  // 基础 url 地址
  baseURL: "http://localhost:5000",
  // 超时时间
  timeout: 10000,
  // 头信息
  headers: { "content-type": "application/json" },
});

// axios 的 HOOK 函数，在发送请求前会主动的调用此函数
instance.interceptors.request.use(function(config) {
  //  如果 token 存在并且发送的不是登陆接口的话，就把 token 加入到认证中
  if (localStorage.getItem("token") && config.url != "/login") {
    config.auth = { username: localStorage.getItem("token"), password: "" };
  }
  return config;
});

// 如果发送的请求，响应的信息内有错误，会回调 error 中的内容
instance.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => {
    // 如果请求结果状态码是 401 的话，代表校验失败
    // 此时需要跳转到登陆界面，同时清理 token
    if (error.response) {
      if (error.response.status == 401) {
        // 清除 token
        localStorage.removeItem("token");
        // 替换最上层路由的页面
        router.replace({ name: "Login" });
        // 拒绝请求
        return Promise.reject(error);
      }
    }
  }
);
// 导入实例
export default instance;
