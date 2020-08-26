import { MutationTree } from 'vuex';
import { TypesStore } from './@types/auth-types';

const mutations: MutationTree<TypesStore.AuthState> = {
    [TypesStore.AuthActions.SIGN_IN](state, payload : TypesStore.AuthLoginVerifiy) {
      if(payload.username === "mark2" && payload.password === "mark2"){
      }
      else {
        console.log("mal",payload);
      }
    },
    [TypesStore.AuthActions.ASK_RECOVER_PASSWORD](state,payload: TypesStore.AuthLoginAskPassword) {

    }
};

export default mutations;