import axios from "./http";
// const 代表定义一个常量
const user = {
  login(loginData) {
    // 使用 axios 的 get 方法发送 get 请求，其中 auth 代表校验，和 Requests 的 auth 参数相同
    return axios.get("/login", { auth: loginData });
  },
};

export default user;
