import Vue from "vue";
import Vuex  from "vuex";
import auth from "@/store/modules/auth/auth";
import workers from "@/store/modules/workers/workers";
Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    auth,
    workers,
  },
});
