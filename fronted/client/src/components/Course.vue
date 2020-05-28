<template>
    <div class="text-left  m-2 border" @click="goInfo">
        <van-row style="padding-bottom: 0px;height: 7rem">
            <van-col span="8" style="padding-bottom: 0px;margin-bottom: 0px">
                <van-image :src="this.$axios.defaults.baseURL+'file/get/'+this.cover"
                           width="6rem"
                           height="7rem"
                           fit="cover"
                >
                    <template v-slot:loading>
                        <van-loading type="spinner" size="20" />
                    </template>
                    <template v-slot:error>加载失败</template>
                </van-image>
            </van-col>
            <van-col span="16" class="pt-2">
                <h5>
                    {{ this.name }}
                </h5>
                <div class="mt-1 small">
                    {{ this.getDate(this.created_at) }}
                </div>
                <div class="mt-3 pt-1 pb-0 d-flex justify-content-between pr-2">
                    <p class="small">作者:{{ this.admin }}  收藏量:{{ this.collect_num ? this.collect_num:0}}</p>
                    <p class="small">{{ this.module}}</p>
                </div>
            </van-col>
        </van-row>
    </div>
</template>

<script>
    import moment from 'moment'
    moment.locale('zh-cn')
    export default {
        name: "Course",
        props:['cover','name','created_at','admin','collect_num','module','course_id'],
        methods:{
            getDate(date)
            {
                return moment(date).fromNow()
            },
            goInfo()
            {
                this.$router.push({path:'/course/info',query:{id:this.course_id}})
            }
        }
    }
</script>

<style scoped>

</style>