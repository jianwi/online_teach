<template>
    <div>
        <van-row class="mt-3 mx-2">
            <van-col :span="8">
                <el-upload
                        class="avatar-uploader"
                        :action="this.$axios.defaults.baseURL + 'file/upload/'"
                        :show-file-list="false"
                        :on-success="handleAvatarSuccess"
                >
                    <img v-if="imageUrl" :src="imageUrl" class="avatar">
                    <i v-else class="el-icon-plus avatar-uploader-icon"></i>
                </el-upload>
            </van-col>
            <van-col :span="16" class="pt-5">
                <div>昵称: {{ user_info.name?user_info.name:'未填写' }}</div>
                <div>性别: {{ user_info.sex?user_info.sex:'未填写' }}</div>
                <div>年龄: {{ user_info.age?user_info.age:'未填写' }}</div>
            </van-col>
        </van-row>
        <hr>
        <van-button block type="default" class="mb-2" to="mine/loved">我的收藏</van-button>
        <van-button block type="default" class="mb-2" to="/mine/comments">评论中心</van-button>
        <van-button block type="default" class="mb-2" to="/mine/modules">栏目管理</van-button>
        <van-button block type="default" class="mb-2">设置</van-button>
        <van-button block type="default" class="mb-2">退出</van-button>



    </div>
</template>

<script>
    export default {
        name: "Mine",
        data() {
            return {
                user_info:'',
                imageUrl: '',
            }
        },
        methods: {
            handleAvatarSuccess(res, file) {
                this.imageUrl = this.$axios.defaults.baseURL + "file/get/" + res
                this.$axios.post("front/user/info/avatar/change/"+res).then(res=>{
                    this.$toast.success("头像修改成功")
                })
            }
        },
        mounted() {
            this.$axios.get('front/user/info').then(res=>{
                this.user_info = res.data.data

                if (this.user_info.avatar){
                    this.imageUrl = this.$axios.defaults.baseURL + "file/get/" +  this.user_info.avatar
                }
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