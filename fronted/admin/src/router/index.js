import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from "../views/auth/Login";
import Register from "../views/auth/Register";
import CompleteInfo from "../views/CompleteInfo";
import CourseAdd from "../views/courses/Add";
import CourseList from "../views/courses/List";
import Module from "../views/courses/Module";
import CommentList from "../views/Comment/List";

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    children: [
      {
        path: '/course/add',
        component: CourseAdd
      },
      {
        path: '/course/list',
        component: CourseList
      },
      {
        path: '/course/module',
        component: Module
      },
      {
        path: '/comment/list',
        component: CommentList
      }
    ]
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
    {
      path: "/auth/login",
      name: "login",
      component: Login
    },
    {
      path: "/auth/register",
      name: "register",
      component: Register
    },
    {
      path: "/complete_info",
      component: CompleteInfo
    }
]

const router = new VueRouter({
  routes
})

export default router
