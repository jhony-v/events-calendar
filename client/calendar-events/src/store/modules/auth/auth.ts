import { Module } from "vuex";
import getters from "./getters";
import mutations from "./mutations";
import actions from "./actions";
import { TypesStore } from './@types/auth-types';

const state: TypesStore.AuthState = {
  id: 1,
  avatar: "avatar",
  password: "mark2",
  username: "mark2",
};

const namespaced: boolean = true;

const auth: Module<TypesStore.AuthState, TypesStore.RootState> = {
  namespaced,
  state,
  getters,
  mutations,
  actions,
};

export default auth;
