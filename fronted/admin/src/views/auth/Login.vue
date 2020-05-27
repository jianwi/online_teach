<template>
  <el-row align="middle" class="wrapper" justify="center" type="flex">
    <el-form :model="form" label-width="80px" ref="form">
      <el-form-item label="用户名">
        <el-input v-model="form.account"></el-input>
      </el-form-item>
      <el-form-item label="密码">
        <el-input type="password" v-model="form.password"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button @click="login" type="primary">登录</el-button>
        <el-button @click="register" type="primary" >注册账户</el-button>
      </el-form-item>
    </el-form>
  </el-row>
</template>

<script>
export default {
  data() {
    return {
      form: {
        account: '',
        password: ''
      }
    }
  },
  methods: {
    register(){
      this.$router.push('/auth/register')
    },
    login() {
      if (!this.form.account) {
        this.$message.error('用户名不能为空')
        return
      }
      if (!this.form.password) {
        this.$message.error('密码不能为空')
        return
      }
      this.$axios({
        url: '/admin_auth/login',
        method: 'post',
        data: this.form
      }).then(res => {
        console.log(res)
        if (res.data.message == '登录成功') {
          localStorage.setItem('token', res.data.data.token)
          localStorage.setItem('user', JSON.stringify(res.data.data.user))
          this.$router.push('/')
        } else {
          this.$message.error('请输入正确的账号和密码')
        }
      }).catch(error => {
        this.$message.error('注册失败，请稍后再试')
      })
    },
    reset() {
      this.form = {
        username: '',
        password: ''
      }
    }
  }
}
</script>

<style lang="less" scoped>
.wrapper {
  position: absolute;
  top: 0;
  bottom: 0;
  width: 100%;
}
</style>
