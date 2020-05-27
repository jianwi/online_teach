<template>
  <div class="mt-5">
    <el-row>
      <el-col :span="8" :offset="4">
        <img :src="user.avatar" class="avatar">
      </el-col>
      <el-col :span="8">
        <div class="text-left font-weight-bolder p-4">
          <el-row>
            <el-col>用户名: {{ user.name }}</el-col>
          </el-row>
          <br />
          <el-row>
            <el-col>发布数: {{ user.post_num?user.post_num:0 }}</el-col>
          </el-row>
        </div>
      </el-col>
    </el-row>
    <hr class="mt-5">
    <el-row :gutter="20">
      <el-col :span="8">
        <router-link to="/course/add" class="btn btn-outline-primary">发布课程</router-link>
      </el-col>
      <el-col :span="8">
        <router-link to="/course/list" class="btn btn-outline-primary">课程管理</router-link>
      </el-col>
      <el-col :span="8">
        <router-link to="/comment/list" class="btn btn-outline-primary">评论管理</router-link>
      </el-col>
    </el-row>
    <el-divider></el-divider>
    <router-view/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  components: {
    HelloWorld
  },
  data(){
    return {
      user: {
        avatar: "",
        post_num: "",
        name: ""
      }
    }
  },
  mounted(){
    this.$axios.get("admin/user/info").then(res=>{
      console.log(res)
      this.user = res.data.data
      this.user.avatar = this.$axios.defaults.baseURL + "file/get/" + res.data.data.avatar
    })
  }
}
</script>
<style scoped>
  .avatar{
    width: 130px;
    height: 130px;
    border-radius: 50%;
  }
</style>