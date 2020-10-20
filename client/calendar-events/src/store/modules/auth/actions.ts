import { UserNamespace } from '@/infraestructure/entities';
import AuthPersistStorageService from '@/infraestructure/services/AuthPersistStorageService';
import AuthService, { AuthServiceAdapter } from '@/infraestructure/services/AuthService';
import router from '@/router';
import { ActionTree } from "vuex";
import { AuthStore } from './auth-types';

const authService : AuthServiceAdapter = new AuthService();

const actions: ActionTree<AuthStore.AuthState, AuthStore.RootState> = {
  
  /**
   * Sign in to the app
   */
  async authSignIn({ commit }, payload: UserNamespace.UserAuth) {
    if(payload.email !== "" && payload.password !== "") {
      commit(AuthStore.AuthActions.LOADING);
      const { token , user } = await authService.signIn(payload);
      AuthPersistStorageService.setValue(token)
      commit(AuthStore.AuthActions.SIGN_IN_COMPLETE,user);
    }
  },

  async authCheckUser({ commit }) {
    commit(AuthStore.AuthActions.LOADING);
    try {
      const { token, validToken, user } = await authService.authVerify(AuthPersistStorageService.getValue());
      if(validToken) {
        AuthPersistStorageService.setValue(token);
        commit(AuthStore.AuthActions.SIGN_IN_COMPLETE,user);
      }
      else {
        router.replace("/sign-in");
      }
    }
    catch(e) {
      router.replace("/sign-in");
    }
  },
  
  authAskRecoverPassword({commit}, payload) {
  }

};

export default actions;
