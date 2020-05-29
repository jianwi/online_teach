<template>
    <div>
        <van-nav-bar
                title="我的收藏"
                left-text="返回"
                left-arrow
                @click-left="$router.back()"
        />
        <course :name="course.name"
                :cover="course.cover"
                :admin="course.admin.name"
                :collect_num="course.collect_num"
                :created_at="course.created_at"
                :module="course.module"
                :key="index"
                :course_id="course.id"
                v-for="(course,index) in list"></course>
    </div>
</template>

<script>
    import Course from "../../components/Course";
    export default {
        name: "Loved",
        components: {Course},
        data(){
            return {
                list:[]
            }
        },
        mounted(){
            this.$axios.get("front/course/loved/all/list").then(res=>{
                this.list = res.data.data
            })
        }
    }
</script>

<style scoped>

</style>