<template>
    <div class="container py-5">
        <h4>用户登录</h4>
        <p class="py-5"></p>
        <van-form @submit="onSubmit">
            <van-field
                    v-model="account"
                    name="account"
                    label="账号"
                    placeholder="账号"
                    :rules="[{ required: true, message: '请填写用户名' }]"
            />
            <van-field
                    v-model="password"
                    type="password"
                    name="password"
                    label="密码"
                    placeholder="密码"
                    :rules="[{ required: true, message: '请填写密码' }]"
            />
            <div style="margin: 16px;" class="mt-5">
                <van-button class="w-75" type="primary" native-type="submit">
                    提交
                </van-button>
            </div>
        </van-form>
        <div>
            没有账户？请 <router-link to="/auth/register">注册</router-link>
        </div>
    </div>
</template>

<script>

    export default {
        name: "Login",
        mounted(){
            localStorage.removeItem('token')
        },
        data() {
            return {
                account: '',
                password: ''
            }
        },

        components:{
        },
        methods:{

            onSubmit(form){
                console.log(form)
                this.$axios.post("front_auth/login",{
                    account: this.account,
                    password: this.password
                }).then(res=>{
                    if (res.data.message == "登录成功"){
                        this.$toast.success(res.data.message)
                        localStorage.setItem('token', res.data.data.token)
                        localStorage.setItem('user', JSON.stringify(res.data.data.user))
                        this.$router.push('/')
                    }

                }).catch(er=>{
                    this.$toast.fail("登录失败，请重试")
                })

            }
        }
    }
</script>

<style scoped>

</style>
