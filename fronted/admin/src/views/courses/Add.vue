<template>
    <div class="pr-3">
        <el-form v-model="form" label-position="right" label-width="80px">
            <el-row>
                <el-col :span="12">
                    <el-form-item label="标题">
                        <el-input v-model="form.name"></el-input>
                    </el-form-item>
                </el-col>
                <el-col :span="12">
                    <el-form-item label-position="right" label="模块">
                        <el-select
                                v-model="form.module"
                                filterable
                                allow-create
                                default-first-option
                                placeholder="请选择课程模块"
                        >
                            <el-option
                                    v-for="item in options"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                            </el-option>
                        </el-select>
                    </el-form-item>
                </el-col>
            </el-row>
            <el-form-item label="封面">
                <el-upload
                        class="cover-uploader"
                        :action="this.$axios.defaults.baseURL + 'file/upload/'"
                        :show-file-list="false"
                        :on-success="handleCoverSuccess"
                >
                    <img v-if="imageUrl" :src="imageUrl" class="avatar">
                    <i v-else class="el-icon-plus avatar-uploader-icon"></i>
                </el-upload>
            </el-form-item>
            <el-row>
                <el-col :span="12">
                    <el-form-item label="类型">
                        <el-radio-group v-model="form.type">
                            <el-radio :label="1">文章</el-radio>
                            <el-radio :label="2">视频</el-radio>
                        </el-radio-group>
                    </el-form-item>
                </el-col>
            </el-row>

            <div>
                <el-form-item label="内容"  v-if="form.type===1">
                    <vue-editor
                            id="editor"
                            :editor-toolbar="customToolbar"
                            useCustomImageHandler
                            @image-added="handleImageAdded"
                            v-model="form.content">
                    </vue-editor>
                </el-form-item>

                <el-form-item label="视频" v-if="form.type===2">
                    <el-upload
                            :action="this.$axios.defaults.baseURL + 'file/upload/'"
                            :multiple="false"
                            :limit="1"
                            :on-success="handleSuccessUploadVideo"
                    >
                        <el-button type="primary">点击上传</el-button>
                    </el-upload>
                </el-form-item>
                <el-form-item>
                    <el-button @click="onSubmit" type="primary">{{ this.postId?"提交修改":"添加" }}</el-button>
                </el-form-item>
            </div>

        </el-form>
    </div>
</template>

<script>
    import {VueEditor} from 'vue2-editor'

    export default {
        name: "Add",
        components: {
            VueEditor
        },
        data() {
            return {
                postId:this.$route.query.id,
                imageUrl: '',
                form: {
                    name: '',
                    module: '',
                    content: '',
                    type: 1,
                    cover: ''
                },
                options: [],
                customToolbar: [
                    ["bold", "italic", "underline"],
                    [{list: "ordered"}, {list: "bullet"}],
                    ["image", "code-block"]
                ]
            }
        },
        mounted() {
            this.$axios.get("api/modules").then(res => {
                this.options = res.data.data
            })

        //   修改
            if(this.postId)
            {
                this.$axios(
                    {
                        url:'/api/course/get/'+this.postId,
                        methods:'get'
                    }
                ).then(res => {
                    console.log(res.data.data)
                        this.form = res.data.data
                    console.log("得到form",this.form)
                        this.imageUrl = this.$axios.defaults.baseURL + "file/get/" + this.form.cover
                    }
                )
            }

        },
        methods: {
            handleCoverSuccess(res) {
                this.imageUrl = this.$axios.defaults.baseURL + "file/get/" + res
                this.form.cover = res
            },
            handleSuccessUploadVideo(res) {
                this.form.content = res
            },
            handleImageAdded: function (file, Editor, cursorLocation, resetUploader) {
                let formData = new FormData();
                formData.append("file", file);

                this.$axios({
                    url: "file/upload/",
                    method: "POST",
                    data: formData
                })
                    .then(res => {
                        let url = this.$axios.defaults.baseURL + "file/get/" + res.data; // Get url from response
                        Editor.insertEmbed(cursorLocation, "image", url);
                        resetUploader();
                    })
                    .catch(err => {
                        console.log(err);
                    });
            },
            onSubmit() {
                this.$axios(
                    {
                        url: this.postId ? '/admin/course/edit/' + this.postId : '/admin/course/add',
                        method: 'POST',
                        data: this.form
                    }
                ).then(res => {
                    console.log(res.data)
                    this.$message.success('添加成功')
                }).catch(error=>{
                    this.$message.error("添加失败了，再试一次吧")
                })
            }
        }

    }
</script>

<style scoped>

</style>