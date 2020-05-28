<template>
    <div>
        <van-nav-bar
                title="课程详情"
                left-text="返回"
                left-arrow
                @click-left="$router.back()"
        />
        <p class="mt-2 h5 text-left pl-3">
            {{ this.course_info.name }}
        </p>
        <p class="small text-left pl-3">
            {{ this.date_time }}
            <span>收藏: </span> {{ this.course_info.col_num }}
        </p>
    </div>
</template>

<script>
    import moment from 'moment'

    moment.locale('zh-cn')
    export default {
        name: "Info",
        data() {
            return {
                course_id: this.$route.query.id,
                course_info: {}
            }
        },
        computed: {
            date_time() {
                return moment(this.course_info.created_at).fromNow()
            }
        },
        methods: {},
        mounted() {
            this.$axios.get("api/course/get/" + this.course_id).then(res => {
                this.course_info = res.data.data
            })

        }

    }
</script>

<style scoped>

</style>