export namespace TypesStore {
  export interface RootState {
    version?: string;
    entered?: string;
  }
  export interface AuthLoginVerifiy {
    username?: string;
    password?: string;
  }
  export interface AuthLoginAskPassword {
    username ?: string;
    email ?: string;
  }
  export interface AuthState extends AuthLoginVerifiy {
    id: number;
    avatar?: string;
  }
  export enum AuthActions {
    SIGN_IN = "SIGN_IN",
    LOG_OUT = "LOG_OUT",
    SIGN_UP = "SIGN_UP",
    ASK_RECOVER_PASSWORD = "ASK_RECOVER_PASSWORD"
  }
}
