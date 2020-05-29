import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from "../views/auth/Login";
import Register from "../views/auth/Register";
import CourseInfo from "../views/Course/Info";
import Mine from "../views/Mine/Index";
import MineLoved from "../views/Mine/Loved";
import Comments from "../views/Mine/Comments";
import MyModule from "../views/Mine/Module";


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
      path: '/mine/modules',
      component: MyModule
    }

]

const router = new VueRouter({
  routes
})

export default router
