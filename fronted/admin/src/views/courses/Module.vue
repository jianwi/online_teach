<template>
    <div>
        <div v-for="item in list">

        </div>
    </div>
</template>

<script>
    export default {
        name: "Module",
        data(){
            list: []

        },
        mounted() {
            this.$axios.get()
        }
    }
</script>

<style scoped>

</style>