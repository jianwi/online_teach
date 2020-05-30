<template>
    <div class="mb-3">
        <p class="text-left">
            <span class="ml-3 font-weight-bolder">{{ i.from_user.name}}</span>
            回复了你的课程
            <span class="ml-3 font-weight-bolder">{{ i.course.name}}</span>:

        </p>
        <p class="bg-light text-left px-5">
            {{ i.content}}
        </p>
        <div class="d-flex mx-5">
            <textarea v-model="content" class="form-control w-75"></textarea>
            <button class="btn btn-primary h-25 mx-3" @click="reply">回复</button>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Comment",
        data(){
            return{
                content:''
            }
        },
        props:['i'],
        methods:{
            reply()
            {
                if (this.content == "") return this.$toast.fail("请输入评论内容呀！！！")
                this.$axios.post("admin/comment/reply",{
                    course_id: this.i.course.id,
                    content: this.content,
                    to: this.i.from_user.id
                }).then(res=>{
                    this.$message("评论成功")
                    this.content = ""
                    this.loadComments()
                })
            }
        }
    }
</script>

<style scoped>

</style>