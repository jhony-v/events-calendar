import { ActionTree } from "vuex";
import { TypesStore } from '@/store/@types';

const actions: ActionTree<TypesStore.AuthState, TypesStore.RootState> = {
  authSignIn({ commit }, payload: TypesStore.AuthActions) {
    commit(TypesStore.AuthActions.SIGN_IN, payload);
  },
};

export default actions;
