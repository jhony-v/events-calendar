import { MutationTree } from 'vuex';
import { AuthStore } from './auth-types';

const mutations: MutationTree<AuthStore.AuthState> = {
    [AuthStore.AuthActions.LOADING](state) {
      state.loading = true;
    },
    
    [AuthStore.AuthActions.SIGN_IN_COMPLETE](state, {token,user} : AuthStore.AuthState) {
      state.loading = false;
      state.failed = false;
      state.token = token;
      state.user = user;
    },

    [AuthStore.AuthActions.SIGN_IN_FAILED](state) {
      state.failed = true;
      state.loading = false;
    }   
};

export default mutations;