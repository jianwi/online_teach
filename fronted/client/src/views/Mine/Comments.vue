<template>
    <div>
        <van-nav-bar
                title="评论管理"
                left-text="返回"
                left-arrow
                @click-left="$router.back()"
        />



        <div class="mt-3 pb-5 text-left">
            <reply

                    :comment_id="i.id"
                    :avatar="i.from_user.avatar"
                    :content="i.content"
                    :from="i.from_user.name"
                    :key="k"
                    :created_at="i.created_at"
                    to_name="我"
                    :course_name="i.course.name"
                    v-for="(i,k) in replies"
            ></reply>

            <reply
                    from="我"
                    :comment_id="i.id"
                    :avatar="i.from_user.avatar"
                    :content="i.content"
                    :name="i.from_user.name"
                    :key="k"
                    :created_at="i.created_at"
                    :to_name="i.to_user.name"
                    :course_name="i.course.name"
                    v-for="(i,k) in comments"
            ></reply>
        </div>
    </div>
</template>

<script>


    import Reply from "../../components/Reply";
    export default {
        name: "Comments",
        components: {Reply},
        data() {
            return {
                comments: [],
                replies: []
            }
        },
        mounted() {
            this.$axios.get('front/my/comments/list').then(res=>{
                this.comments = res.data.data
            })
            this.$axios.get('front/my/reply/list').then(res=>{
                this.replies = res.data.data
            })
        }
    }
</script>

<style scoped>

</style>