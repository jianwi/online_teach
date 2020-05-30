<template>
    <div>
            <van-search
                    v-model="keywords"
                    placeholder="请输入搜索关键词"
                    @search="search"
                    show-action
                    @cancel="$router.push('/')"
            />
            <div>
                    <van-button block v-for="(item,index) in history" :key="index" :title="item"
                        @click="btn_s(item)"
                    >
                        {{ item }}
                    </van-button>
            </div>
    </div>
</template>

<script>
    export default {
        name: "Search",
        data(){
            return{
                keywords:'',
                history:''
            }
        },
        methods:{
            search()
            {
                this.$router.push({
                    path: '/',
                    query: {
                        key: this.keywords
                    }
                })
            },
            btn_s(k)
            {
                this.keywords = k
                this.search()
            }
        },
        mounted(){
            this.$axios.get("front/my/search/history").then(res => {
                this.history = res.data.data.reverse()
            })
        }
    }
</script>

<style scoped>

</style>