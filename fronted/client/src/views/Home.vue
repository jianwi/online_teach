<template>
    <div>
        <van-row type="flex" justify="space-between">
            <van-col span="4" class="pt-1">
                <van-image src=""
                           round
                           width="2.5rem"
                           height="2.5rem"
                           @click="goMine"
                >
                    <template v-slot:error>头像</template>
                </van-image>
            </van-col>
            <van-col span="20">
                <van-search
                        placeholder="请输入搜索关键词"
                        @click="goSearch"
                />
            </van-col>
        </van-row>
        <!--    分类 -->
        <div class="d-flex flex-wrap">
            <van-button class="mx-1" size="small" type="info" :key="index" v-for="(item,index) in modules">{{ item.value }}</van-button>
        </div>

<!--      course list-->
      <div>
        <course :name="course.name"
                :cover="course.cover"
                :admin="course.admin.name"
                :collect_num="course.collect_num"
                :created_at="course.created_at"
                :module="course.module"
                :key="index"
                :course_id="course.id"
                v-for="(course,index) in courses"></course>
      </div>
    </div>
</template>

<script>
  import Course from "../components/Course";
    export default {
        name: 'Home',
        components: { Course },
        data() {
            return {
                modules: [],
                courses: []
            }
        },
        methods: {
            goSearch() {
                this.$router.push("/sss")
            },
            goMine() {
                this.$router.push('/mine')
            },

        },
        mounted() {
          this.$axios.get("api/modules").then(res=>{
            this.modules = res.data.data
          })

            this.$axios.get("api/course/all").then(res=>{
                this.courses = res.data.data
            })
        }
    }
</script>
