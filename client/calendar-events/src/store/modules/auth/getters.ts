import { GetterTree } from "vuex";
import { AuthStore } from './auth-types';

const getters: GetterTree<AuthStore.AuthState, AuthStore.RootState> = {
    isAuthentication : state => !!state.token
};
export default getters;