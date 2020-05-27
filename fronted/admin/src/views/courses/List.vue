<template>
    <div class="">
        <ul class="border-bottom pb-1" v-for="item in lists">
           <el-row>
               <el-col :span="18">
                   <p class="font-weight-bolder" style="font-size: 18px">
                       {{ item.name }}
                   </p>
               </el-col>
               <el-col :span="3">
                   <el-button type="primary" icon="el-icon-edit" circle size="small" @click="goEdit(item.id)"></el-button>
               </el-col>
               <el-col :span="3">
                   <el-button type="danger" icon="el-icon-delete" circle size="small" @click="deleteCourse(item.id)"></el-button>
               </el-col>
           </el-row>
        </ul>
    </div>
</template>

<script>
    export default {
        name: "List",
        data() {
            return {
                lists: []
            }
        },
        mounted() {
            this.loadList()
        },
        methods:{
            loadList(){
                this.$axios.get("admin/course/list").then(res=>{
                    this.lists = res.data.data
                })
            },
            goEdit(id){
                console.log(id)
                this.$router.push({
                    path:'/course/add',
                    query: {id:id}
                })
            },
            deleteCourse(id){
                if (!confirm("确认删除此课程？")) return
                this.$axios.post("admin/course/delete/"+id).then(res=>{
                    if (res.data.code == 200){
                        this.$message.success("课程删除成功！")
                        this.loadList()
                    }else {
                        this.$message.error(res.data.message)
                    }
                }).catch(error=>{
                    this.$message.error("课程删除失败！")
                })
            }
        }
    }
</script>

<style scoped>

</style>