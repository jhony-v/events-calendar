import { TypesStore } from '@/store/@types';
import { MutationTree } from 'vuex';

const mutations: MutationTree<TypesStore.AuthState> = {
    [TypesStore.AuthActions.SIGN_IN](state, payload : TypesStore.AuthLoginVerifiy) {
      if(payload.username === "mark2" && payload.username === "mark2"){
        console.log("ok");
      }
      else {
        console.log("mal",payload);
      }
    },
};

export default mutations;