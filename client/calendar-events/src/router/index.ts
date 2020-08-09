import Vue from "vue";
import VueRouter, { RouteConfig } from "vue-router";

Vue.use(VueRouter);

const routes: Array<RouteConfig> = [
  {
    path: "/",
    name: "Home",
    component: () => import("../views/Home/Home.vue"),
  },
  {
    path: "/about/:id",
    name: "About",
    component: () => import("../views/About/About.vue"),
  },
  {
    path : "/sign-in",
    name : "SignIn",
    component : () => import("../views/Auth/Auth.vue"),
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
