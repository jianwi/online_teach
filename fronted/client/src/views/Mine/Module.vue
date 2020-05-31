<template>
    <div>
        <van-nav-bar
                title="模块管理"
                left-text="返回"
                left-arrow
                @click-left="$router.back()"
        />
        <div>
            <hr>
            <div  v-for="(i,k) in modules_have" :key="k" class="border-bottom d-flex justify-content-between p-2" >
                {{ i.value }}
                <button @click="cancleFollowIt(i.id)" class="btn btn-danger">
                    删除
                </button>
            </div>
        </div>
        <div>
            <div v-for="(i,k) in all_modules" :key="k" class="border-bottom d-flex justify-content-between p-2">
                {{ i.value }}

                <button @click="followIt(i.id)" class="btn btn-primary">
                    关注
                </button>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Module",
        data(){
            return {
                modules_have:[],
                all_modules:[]
            }
        },
        mounted(){
            this.loadModule()
        },
        methods:{
            loadModule(){
                this.$axios.get("front/modules").then(res => {
                    this.all_modules = res.data.data
                })
                this.$axios.get("front/modules/have").then(res => {
                    this.modules_have = res.data.data
                })

                this.all_modules = this.all_modules.filter(item=>{
                    return item
                })
            },
            followIt(id)
            {
                this.$axios.post('front/modules/follow/'+id).then(res=>{
                    if (res.data.code == 200){
                        this.$toast.success("已关注")
                        this.loadModule()
                    }
                })
            },
            cancleFollowIt(id)
            {
                if (!confirm("确认删除")) return
                this.$axios.post('front/modules/cancel/'+id).then(res=>{
                    if (res.data.code == 200){
                        this.$toast.success("已取消关")
                        this.loadModule()
                    }
                })
            }
        }
    }
</script>

<style scoped>

</style>