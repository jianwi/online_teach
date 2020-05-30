import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from "../views/auth/Login";
import Register from "../views/auth/Register";
import CourseInfo from "../views/Course/Info";
import Mine from "../views/Mine/Index";
import MineLoved from "../views/Mine/Loved";
import Comments from "../views/Mine/Comments";
import Setting from "../views/Mine/Setting";
import Search from "../views/Course/Search";


Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
    {
      path: "/auth/login",
      component: Login
    },
    {
      path: "/auth/register",
      component: Register
    },
    {
      path: '/course/info',
      component: CourseInfo
    },
    {
      path: '/mine',
      component: Mine
    },
    {
      path: '/mine/loved',
      component: MineLoved
    },
    {
      path: '/mine/comments',
      component: Comments
    },
    {
      path: '/mine/settings',
      component: Setting
    },
    {
      path: '/course/search',
      component: Search
    }

]

const router = new VueRouter({
  routes
})

export default router
