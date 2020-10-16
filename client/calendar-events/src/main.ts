import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import moment from "moment";
import "./router/routerAuthCheck";
import PortalVue from "portal-vue";
// moment.locale("es");


Vue.use(PortalVue);
Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
