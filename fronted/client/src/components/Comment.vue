<template>
    <div class="border-bottom p-2">
        <van-row>
            <van-col :span="4">
                <van-image :src="this.$axios.defaults.baseURL+'file/get/'+this.avatar"
                           width="3.5rem"
                           height="3.5rem"
                           round
                           fit="cover"
                >
                    <template v-slot:loading>
                        <van-loading type="spinner" size="20" />
                    </template>
                    <template v-slot:error>加载失败</template>
                </van-image>
            </van-col>

            <van-col :span="18" class="text-left">
                <p class="small">
                    {{ this.name }}
                    <span class="ml-3 pl-3">{{ this.getDate(this.created_at) }}</span>
                </p>
                <div class="bg-light">
                    {{ this.content }}
                </div>
            </van-col>
        </van-row>
    </div>
</template>

<script>
    // import moment from 'moment'
    import moment from 'moment-timezone'
    moment.locale('zh-cn')
    moment.tz.setDefault("Asia/Shanghai");
    export default {
        name: "Comment",
        props:['avatar','name','created_at','content','comment_id'],
        methods:{
            getDate(date)
            {
                return moment(date).utcOffset(+0).format('YYYY-MM-DD HH:mm:ss');
            },
        }
    }
</script>

<style scoped>

</style>