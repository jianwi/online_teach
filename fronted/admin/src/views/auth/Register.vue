<template>
    <el-row align="middle" class="wrapper" justify="center" type="flex">
        <el-form :model="form" label-width="80px" ref="form">
            <el-form-item label="账户">
                <el-input v-model="form.account"></el-input>
            </el-form-item>
            <el-form-item label="密码">
                <el-input type="password" v-model="form.password"></el-input>
            </el-form-item>
            <el-form-item>
                <el-button @click="register" type="primary">注册</el-button>
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
            register() {
                if (!this.form.account) {
                    this.$message.error('用户名不能为空')
                    return
                }
                if (!this.form.password) {
                    this.$message.error('密码不能为空')
                    return
                }
                this.$axios({
                    url: '/admin_auth/register',
                    method: 'post',
                    data: this.form
                }).then(res => {
                    console.log(res)
                    if (res.data.message == 'register success') {
                        this.$message.success("注册成功！")
                        this.$router.push('/auth/complete')
                    } else {
                        this.$message.error('注册失败，请稍后再试')
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
