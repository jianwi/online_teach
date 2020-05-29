<template>
    <div>
        <van-nav-bar
                title="我的收藏"
                left-text="返回"
                left-arrow
                @click-left="$router.back()"
        />
        <hr>
        <div>
            我关注的栏目
        </div>

    </div>
</template>

<script>
    export default {
        name: "Module"
    }
</script>

<style scoped>

</style>