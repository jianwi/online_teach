<template>
    <div class="border-bottom p-2">
        <div>
            <span class="font-weight-bolder">我</span> 评论了 <span class="font-weight-bolder">{{ to_name}}</span>:
<!--            <div class="bg-info text-light">-->
<!--                {{ course_name }}-->
<!--            </div>-->
            <div class="font-weight-bolder">{{content}}</div>
        </div>
    </div>
</template>

<script>
    import moment from 'moment'
    moment.locale('zh-cn')
    export default {
        name: "Comment",
        props:['avatar','name','created_at','content','comment_id','to_name','course_name'],
        methods:{
            getDate(date)
            {
                return moment(date).fromNow()
            },
        }
    }
</script>

<style scoped>

</style>