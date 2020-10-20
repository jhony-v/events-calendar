import { API } from "../config/api";
import { UserNamespace } from "../entities";


export interface AuthServiceAdapter {
  signIn( authenticationUser: UserNamespace.UserAuth ): Promise<UserNamespace.UserAuthResponse>;
  authVerify(token : string ): Promise<UserNamespace.UserAuthResponse>;
}


export default class AuthService implements AuthServiceAdapter {

  /**
   * Start session
   * @param authenticationUser email and password user to sign in
   */
  signIn = async (authenticationUser: UserNamespace.UserAuth) => {
    try {
      const request = await API.post<UserNamespace.UserAuthResponse>("auth/sign-in", {
        email: authenticationUser.email,
        password: authenticationUser.password,
      });
      return request.data;
    } catch (e) {
      throw new Error(e);
    }
  };

  /**
   * Check the token
   * @param token verify the token saved in local storage
   */
  authVerify = async (token : string ) => {
    try {
      const request = await API.post<UserNamespace.UserAuthResponse>("auth/verify", {
        token
      })
      return request.data;
    }catch(e) {
      throw new Error(e);
    }
  } 

}
