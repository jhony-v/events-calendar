import { Module } from "vuex";
import getters from "./getters";
import mutations from "./mutations";
import actions from "./actions";
import { AuthStore } from "./auth-types";
import AuthServicePersistStorage from "@/infraestructure/services/AuthPersistStorageService";

const auth: Module<AuthStore.AuthState, AuthStore.RootState> = {
  namespaced: true,
  state: {
    loading: false,
    failed: false,
    user: {},
    token: AuthServicePersistStorage.getValue(),
  },
  getters,
  mutations,
  actions,
};

export default auth;
