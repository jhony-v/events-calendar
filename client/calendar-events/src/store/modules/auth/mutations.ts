import { TypesStore } from '@/store/@types';
import { MutationTree } from 'vuex';

const mutations: MutationTree<TypesStore.AuthState> = {
    [TypesStore.AuthActions.SIGN_IN](state, payload : TypesStore.AuthLoginVerifiy) {
      if(payload.username === "mark2" && payload.password === "mark2"){
      }
      else {
        console.log("mal",payload);
      }
    },
};

export default mutations;