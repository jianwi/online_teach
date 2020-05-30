<template>
    <div>
        <van-row type="flex" justify="space-between">
            <van-col span="4" class="pt-1">
                <van-image :src="imageUrl"
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
                        :value="search_v"
                        @click="goSearch"
                />
            </van-col>
        </van-row>
        <!--    分类 -->
        <div class="d-flex flex-wrap">

            <van-button @click="getFromModule(1)" class="mx-1" size="small" type="info"
            >热门课程
            </van-button>
            <van-button @click="getFromModule(2)" class="mx-1" size="small" type="info"
            >猜你喜欢
            </van-button>

            <van-button @click="getFromModule(item.value)" class="mx-1" size="small" type="info" :key="index"
                        v-for="(item,index) in modules">{{ item.value }}
            </van-button>
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
        components: {Course},
        data() {
            return {
                modules: [],
                courses: [],
                search_v: this.$route.query['key'],
                user_info: '',
                imageUrl: '',
            }
        },
        methods: {
            goSearch() {
                this.$router.push("/course/search")
            },
            goMine() {
                this.$router.push('/mine')
            },
            getFromModule(item) {
                this.$axios.get("api/course/get/from/module/" + item).then(res => {
                    this.courses = res.data.data
                })
            }

        },
        mounted() {
            this.$axios.get('front/user/info').then(res => {
                this.user_info = res.data.data

                if (this.user_info.avatar) {
                    this.imageUrl = this.$axios.defaults.baseURL + "file/get/" + this.user_info.avatar
                }
                if (this.user_info.sex == 1) {
                    this.user_info.sex = "男"
                } else if (this.user_info.sex == 2) {
                    this.user_info.sex = "女"
                }
            })

            this.$axios.get("api/modules").then(res => {
                this.modules = res.data.data
            })

            if (this.search_v) {
                this.$axios.get("front/course/filter/" + this.search_v).then(res => {
                    this.courses = res.data.data
                })
            } else {
                this.$axios.get("api/course/all").then(res => {
                    this.courses = res.data.data
                })
            }
        }
    }
</script>
