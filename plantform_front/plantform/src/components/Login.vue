<template>
  <!-- class 属性，可以设置样式 -->
  <div class="login">
    <h1>登陆</h1>
    <v-text-field
      v-model="message4"
      label="账号"
      outlined
      clearable
    ></v-text-field>
    <!-- type 是 html 的 inpu 的属性，可以设置为 password -->
    <v-text-field
      v-model="message4"
      label="密码"
      outlined
      type="password"
      clearable 
    ></v-text-field>
    <v-btn depressed color="primary"> 登陆 </v-btn>
    <!-- @ 是 vue 的语法，将 click 事件绑定到一个函数  -->
    <v-btn depressed @click="goSignUp()"> 注册 </v-btn>
  </div>
</template>
<script>
export default {
  // methods 代表声明一个函数
  methods: {
    goSignUp() {
      // this.$router.push：把一个路由推入栈
      this.$router.push({ name: "SignUp" });
    },
  },
};
</script>
<style scoped>
/* .代表 class */
.login {
  /* 将长度规定为 500 */
  width: 500px;
  /* 将整个标签居中 */
  margin: 0 auto;
  /* 将文本和按钮居中 */
  text-align: center;
}
</style>