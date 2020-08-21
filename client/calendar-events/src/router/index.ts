import Vue from "vue";
import VueRouter, { RouteConfig } from "vue-router";

Vue.use(VueRouter);

const routes: Array<RouteConfig> = [
  {
    path: "/",
    name: "Home",
    component: () => import("../views/Home/Home.vue"),
    meta : {
      auth : true
    },
  },
  {
    path: "/about/:id",
    name: "About",
    component: () => import("../views/About/About.vue"),
    meta : {
      auth : true
    },
  },
  {
    path : "/sign-in",
    name : "SignIn",
    component : () => import("../views/Auth/Auth.vue"),
  },
  {
    path : "/forgot-password",
    name : "ForgotPassword",
    component : () => import("../views/AuthForgotPassword/AuthForgotPassword.vue"),
  },
  {
    path : "*",
    name : "Error",
    component : () => import("../views/Error/Error404.vue")
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
