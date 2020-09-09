import Vue from "vue";
import VueRouter, { RouteConfig } from "vue-router";
import linkRoutes from "@/constants/links-routes";

Vue.use(VueRouter);

const routes: Array<RouteConfig> = [
  {
    path: linkRoutes.home.default,
    name: "Dashboard",
    component: () => import("../views/Home/Home.vue"),
    meta: {
      auth: true,
    },
    children: [
      {
        path: linkRoutes.home.children.default,
        children: [
          {
            path: linkRoutes.home.children.default,
            component: () => import("../views/Home/HomeScenes/Default/HomeDefaultScene.vue"),
          },
          {
            path : linkRoutes.home.children.newEvent,
            component :() => import("../views/Home/HomeScenes/NewEventDefine/HomeNewEventDefineScene.vue")
          }
        ],
      },
      {
        path: linkRoutes.about.default,
        component: () => import("../views/About/About.vue"),
      },
      {
        path : linkRoutes.settings.default,
        component : () => import("../views/UserSettings/UserSettings.vue")
      },
      {
        path : linkRoutes.explore.default,
        component : () => import("../views/ExploreEvents/ExploreEvents.vue")
      }
    ],
  },
  {
    path: linkRoutes.signIn.default,
    name: "SignIn",
    component: () => import("../views/Auth/Auth.vue"),
  },
  {
    path: linkRoutes.forgotPassword.default,
    name: "ForgotPassword",
    component: () =>
      import("../views/AuthForgotPassword/AuthForgotPassword.vue"),
  },
  {
    path: linkRoutes.error.default,
    name: "Error",
    component: () => import("../views/Error/Error404.vue"),
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
