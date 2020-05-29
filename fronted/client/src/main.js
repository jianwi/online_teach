import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from "axios";
import Vant from 'vant';
import 'vant/lib/index.css';
import {Upload} from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

Vue.use(Upload)

Vue.use(Vant)

import {Toast} from 'vant'

Vue.prototype.$toast = Toast

Vue.config.productionTip = false

Vue.prototype.$axios = axios

axios.defaults.baseURL = 'http://127.0.0.1:5000/'

axios.interceptors.request.use((config) => {
    // console.log(config.headers.Authorization)
    if (!config.headers.Authorization && localStorage.getItem('token')) {
        config.headers.Authorization = 'Bearer ' + localStorage.getItem('token')
    }
    // console.log(config.headers.Authorization)
    return config;
})


// 全局路由守卫
router.beforeEach((to, from, next) => {
    console.log('from:' + from.path)
    console.log('to:' + to.path)
    if (!/^\/auth/.test(to.path)) {
        if (!localStorage.getItem('token')) {
            router.push('/auth/login')
        } else {
            next()
        }
    } else {
        next()
    }

})

new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app')
