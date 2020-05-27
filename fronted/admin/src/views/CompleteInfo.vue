<template>
    <div>
        <h4 class="text-center mt-3 mb-5">完善信息</h4>
        <el-form  v-model="form" label-width="80px">

            <el-row :gutter="20">

                <el-col :span="6">
                    <el-upload
                            class="avatar-uploader"
                            :action="this.$axios.defaults.baseURL + 'file/upload/'"
                            :show-file-list="false"
                            :headers="{Authorization:token}"
                            :on-success="handleAvatarSuccess"
                            :before-upload="beforeAvatarUpload"
                    >
                        <img v-if="imageUrl" :src="imageUrl" class="avatar">
                        <i v-else class="el-icon-plus avatar-uploader-icon"></i>
                    </el-upload>
                </el-col>
                <el-col :span="18">
                    <el-row :gutter="20">
                        <el-col :span="11">
                            <el-form-item label="名称">
                                <el-input v-model="form.name" placeholder="名称"></el-input>
                            </el-form-item>
                        </el-col>
                        <el-col :span="11">
                            <el-form-item label="联系方式">
                                <el-input v-model="form.phone_number" placeholder="联系方式"></el-input>
                            </el-form-item>
                        </el-col>
                    </el-row>
                    <br>
                    <el-row :gutter="20">
                        <el-col :span="11">
                            <el-form-item label="公司/机构">
                                <el-input v-model="form.institution" placeholder="公司/机构"></el-input>
                            </el-form-item>
                        </el-col>
                    </el-row>
                </el-col>
            </el-row>
            <el-row>
                <el-form-item>
                    <el-button type="primary" @click="onSubmit">提交</el-button>
                </el-form-item>
            </el-row>
        </el-form>

    </div>

</template>

<script>
    export default {
        name: "complete_info",
        data() {
            return {
                form: {
                    name: "",
                    avatar: '',
                    phone_number: '',
                    institution: '',
                },
                imageUrl: '',
                token: 'Bearer ' + localStorage.getItem('token'),
            };
        },
        methods: {
            handleAvatarSuccess(res, file) {
                this.imageUrl = this.$axios.defaults.baseURL + "file/get/" + res
                this.form.avatar = res
            },
            beforeAvatarUpload(file) {
                let isJPG = file.type === 'image/jpeg';
                let isLt2M = file.size / 1024 / 1024 < 2;

                if (!isJPG) {
                    this.$message.error('上传头像图片只能是 JPG 格式!');
                }
                if (!isLt2M) {
                    this.$message.error('上传头像图片大小不能超过 2MB!');
                }
                return isJPG && isLt2M;
            },
            onSubmit()
            {
                let form = this.form
                this.$axios.post("admin/complete_info",form).then(res=>{
                    if (res.data.code === 200){
                        this.$message.success("保存成功")
                        this.$router.push("/")
                    }
            }).catch(error=>{
                this.$message.error("出错了，请稍后再试吧")
                })
            }
        },
        created() {
            this.$axios.get("http://127.0.0.1:5000/admin/").then(res => {
                console.log(res)
            })
        }
    }
</script>

<style scoped>
    .avatar-uploader .el-upload {
        border: 1px dashed #d9d9d9;
        border-radius: 6px;
        cursor: pointer;
        position: relative;
        overflow: hidden;
    }

    .avatar-uploader .el-upload:hover {
        border-color: #409EFF;
    }

    .avatar-uploader-icon {
        font-size: 28px;
        color: #8c939d;
        width: 178px;
        height: 178px;
        line-height: 178px;
        text-align: center;
    }

    .avatar {
        width: 138px;
        height: 138px;
        display: block;
        border-radius: 50%;
    }
</style>