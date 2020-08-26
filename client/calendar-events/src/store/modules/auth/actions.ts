import { ActionTree } from "vuex";
import { TypesStore } from './@types/auth-types';

const actions: ActionTree<TypesStore.AuthState, TypesStore.RootState> = {
  authSignIn({ commit }, payload: TypesStore.AuthActions) {
    commit(TypesStore.AuthActions.SIGN_IN, payload);
  },
  authAskRecoverPassword({commit}, payload : TypesStore.AuthLoginAskPassword) {
    commit(TypesStore.AuthActions.ASK_RECOVER_PASSWORD,payload);
  }
};

export default actions;
