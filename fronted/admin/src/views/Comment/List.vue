<template>
    <div>
        <comment
                   v-for="(i,k) in comments"
                   :key="k"
                    :i="i"
        >

        </comment>
        <hr>
        <div class="alert alert-info">
            已回复：
        </div>
        <div v-for="(i,k) in replies" :key="k" class="text-left pl-4 pb-3">
            <p>
                我  回复
                <span class="font-weight-bolder"> {{ i.to_user.name }}</span>
            </p>
            <p>
                {{ i.content}}
            </p>
        </div>
    </div>
</template>

<script>
    import Comment from "../../components/Comment";
    export default {
        name: "List",
        components: {Comment},
        data(){
            return{
                comments:[],
                replies:[]
            }
        },
        mounted()
        {
            this.$axios.get("admin/my/comments/list").then(res=>{
                this.comments = res.data.data
            })

            this.$axios.get("admin/my/reply/list").then(res=>{
                this.replies = res.data.data
            })
        }
    }
</script>

<style scoped>

</style>