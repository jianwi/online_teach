<template>
    <div>
        <van-nav-bar
                class="bg-light"
                title="课程详情"
                left-text="返回"
                left-arrow
                @click-left="$router.back()"
        />
        <p class="mt-2 h5 text-left pl-3 py-1">
            {{ this.course_info.name }}
        </p>
        <p class="small text-left ml-3">
            发布于:{{ this.date_time }}
            <span class="ml-3">收藏量: </span> {{ this.course_info.collect_num? this.course_info.collect_num:"没人收藏" }}
            <span class="ml-3">播放量: </span> {{ this.course_info.view_num? this.course_info.view_num:0 }}
        </p>
        <p class="d-flex justify-content-between mx-3">
            <small>综合评分： {{ this.course_info.score?this.course_info.score:"没有人打分" }}</small>

            <van-button v-if="!loved_it" type="info" size="mini" @click="loveIt">收藏</van-button>
            <van-button v-else type="info" size="mini" @click="dontloveIt">取消收藏</van-button>
        </p>
        <hr>
<!--        课程内容-->
        <div style="width: 100%;overflow: scroll" id="course_content" v-html="this.course_info.content">
        </div>

        <div class="mt-3 text-left ml-3 d-flex justify-content-around">
            <span class="font-weight-bolder small" > 打分：</span>
            <van-rate v-model="star" :readonly="stared" @change="starIt" />
        </div>
        <hr>
<!--        评论区-->
        <div class="mt-3 pb-5">
            <comment
                    :comment_id="i.id"
                    :avatar="i.from_user.avatar"
                    :content="i.content"
                    :name="i.from_user.name"
                    :key="k"
                    :created_at="i.created_at"
                v-for="(i,k) in comments"
            ></comment>
        </div>
<!--        发布评论-->
        <div class="fixed-bottom border-top">
            <van-field
                    v-model="new_comment"
                    center
                    clearable
                    placeholder="评论课程"
            >
                <template #button>
                    <van-button @click="sendComment" size="small" type="primary">发送</van-button>
                </template>
            </van-field>
        </div>
    </div>
</template>

<script>
    import moment from 'moment'
    import Comment from "../../components/Comment";

    moment.locale('zh-cn')
    export default {
        name: "Info",
        components: {Comment},
        data() {
            return {
                course_id: this.$route.query.id,
                course_info: {},
                star:0,
                stared:false,
                new_comment:'',
                comments:[],
                loved_it:false,
            }
        },
        computed: {
            date_time() {
                return moment(this.course_info.created_at).fromNow()
            }
        },
        methods: {
            starIt(star)
            {
                this.$axios.post("front/course/star/post/"+this.course_id+'/'+star).then(res=>{
                    console.log(res)
                    if (res.data.code == 200){
                        this.$toast.success("已打分")
                    }else {
                        this.$toast.fail("打分失败，你已经打过分了")
                        return false
                    }
                }).error(res=>{
                    this.$toast.fail("打分失败，请重试")
                    return false
                })
            },
            sendComment()
            {
                if (this.new_comment == "") return this.$toast.fail("请输入评论内容呀！！！")
                this.$axios.post("front/course/comment/add",{
                    course_id: this.course_id,
                    content: this.new_comment
                }).then(res=>{
                    this.$toast.success("评论成功")
                    this.new_comment = ""
                    this.loadComments()
                })
            },
            loadComments()
            {
                //    加载评论
                this.$axios.get('/api/comment/all/'+this.course_id).then(res=>{
                    this.comments = res.data.data
                })
            },
            loveIt()
            {
                this.$axios.post("front/course/love/"+this.course_id).then(res=>{
                   if (res.data.code==200)
                   {
                       this.loved_it = true
                       this.$toast.success("已收藏")
                   }
                })
            },
            dontloveIt()
            {
                this.$axios.post("front/course/dontlove/"+this.course_id).then(res=>{
                    if (res.data.code==200)
                    {
                        this.loved_it = false
                        this.$toast.success("已取消收藏")
                    }
                })
            }
        },
        mounted() {
            this.$axios.get("api/course/get/" + this.course_id).then(res => {
                this.course_info = res.data.data

                if (this.course_info.type == 2){
                    this.course_info.content = `
                        <video width="98%" src="${this.$axios.defaults.baseURL}file/get/${this.course_info.content}" controls></video>
                    `
                }
            })

        //    获取 我 对此课程的评分
            this.$axios.get('front/course/star/get/'+this.course_id).then(res=>{
               if (res.data.data){
                   this.star = res.data.data
                   this.stared = true
               }else{
                    this.star = 0
               }
            })

            this.loadComments()

        //    if i loved that course?
            this.$axios.get('front/course/loved/'+this.course_id).then(res=>{
                if (res.data.data=="true"){
                    this.loved_it = true
                }
            })
        }

    }
</script>

<style scoped>

</style>