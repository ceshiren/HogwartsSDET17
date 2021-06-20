import axios from "axios";
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
        config.auth = {username: localStorage.getItem("token"), password: ""}
    }
    return config;
});

// 导入实例
export default instance;
