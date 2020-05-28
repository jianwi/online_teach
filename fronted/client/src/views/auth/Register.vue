<template>
    <div class="container py-5">
        <h4>用户注册</h4>
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
                    注册
                </van-button>
            </div>
        </van-form>
    </div>
</template>

<script>
    export default {
        name: "Register",
        mounted() {
            localStorage.removeItem('token')
        },
        data() {
            return {
                account: '',
                password: ''
            }
        },

        components: {},
        methods: {

            onSubmit(form) {
                console.log(form)
                this.$axios.post("/front_auth/register", {
                    account: this.account,
                    password: this.password
                }).then(res => {
                    this.$toast.success("注册成功")
                    this.$router.push("/auth/login")
                }).catch(err=>{
                    this.$toast.fail("注册失败，请重试")
                })
            }
        }
    }
</script>

<style scoped>

</style>