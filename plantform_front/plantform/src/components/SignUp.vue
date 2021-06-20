<template>
  <v-main>
    <!-- class 属性，可以设置样式 -->
    <div class="sign-up">
      <h1>注册</h1>
      <v-text-field
        v-model="username"
        label="账号"
        outlined
        clearable
      ></v-text-field>
      <!-- type 是 html 的 inpu 的属性，可以设置为 password -->
      <v-text-field
        v-model="password"
        label="密码"
        outlined
        type="password"
        clearable
      ></v-text-field>
      <v-text-field
        v-model="email"
        label="邮箱"
        outlined
        clearable
      ></v-text-field>
      <v-btn depressed @click="signUp()" color="primary"> 注册 </v-btn>
      <v-btn depressed @click="goLogin()"> 登陆 </v-btn>
    </div>
  </v-main>
</template>
<script>
export default {
  data() {
    return { username: "", password: "", email: "" };
  },
  methods: {
    signUp() {
      let data = {
        username: this.username,
        password: this.password,
        email: this.email,
      };
      this.$api.user.signUp(data).then((response) => {
        // 后端每一个返回结果，都要有 errcode
        if (response.data.errcode == 200) {
          this.$router.push({"name": "TestCase"})
        }
      });
    },
    goLogin() {
      this.$router.push({ name: "Login" });
    },
  },
};
</script>
<style scoped>
/* .代表 class */
.sign-up {
  /* 将长度规定为 500 */
  width: 500px;
  /* 将整个标签居中 */
  margin: 0 auto;
  /* 将文本和按钮居中 */
  text-align: center;
}
</style>