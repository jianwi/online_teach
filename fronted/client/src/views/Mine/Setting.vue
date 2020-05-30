<template>
    <div>
        <van-nav-bar
                title="设置"
                left-text="返回"
                left-arrow
                @click-left="$router.back()"
        />
        <hr>
        <div>
            <van-form @submit="onSubmit">
                <van-field
                        v-model="form.name"
                        name="name"
                        label="用户名"
                        placeholder="用户名"
                        :rules="[{ required: true, message: '请填写用户名' }]"
                />
                <van-field name="sex" label="性别">
                    <template #input>
                        <van-radio-group v-model="form.sex" direction="horizontal">
                            <van-radio name="1">男</van-radio>
                            <van-radio name="2">女</van-radio>
                        </van-radio-group>
                    </template>
                </van-field>
                <van-field
                        v-model="form.age"
                        type="digit"
                        name="age"
                        label="年龄"
                        :rules="[{ required: true, message: '请填写年龄' }]"
                />
                <van-field
                        v-model="form.describe"
                        rows="2"
                        autosize
                        name="describe"
                        label="介绍"
                        type="textarea"
                        maxlength="50"
                        placeholder="请输入个人介绍"
                        show-word-limit
                />
                <van-field
                        v-model="form.password"
                        type="password"
                        name="password"
                        label="密码"
                        placeholder="密码"
                />
                <div style="margin: 16px;">
                    <van-button round block type="info" native-type="submit">
                        提交
                    </van-button>
                </div>
            </van-form>
        </div>

    </div>
</template>

<script>
    export default {
        name: "Setting",
        data(){
            return {
                form: {
                    name: '',
                    sex: '',
                    age: '',
                    describe: '',
                    password: ''
                }
            }
        },
        methods:{
            onSubmit(form){
                console.log(form);
                if (!form.password){
                    form.password = ""
                }
                this.$axios.post('front/my/info/modify',form).then(res=>{
                    this.$toast.success('修改成功')
                })
            }
        },
        mounted() {
            this.$axios.get('front/user/info').then(res=>{
                this.form = res.data.data
                if (!this.form.describe)
                {
                    this.form.describe = ""
                }
            })
        }

    }
</script>

<style scoped>

</style>