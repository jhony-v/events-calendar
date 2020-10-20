import { UserNamespace } from '@/infraestructure/entities';

export namespace AuthStore {
  export interface RootState {
    version?: string;
    entered?: string;
  }

  export interface AuthState extends UserNamespace.UserAuthResponse {
    loading ?: boolean;
    failed ?: boolean;
  }

  export enum AuthActions {
    LOADING = "LOADING",
    SIGN_IN = "SIGN_IN",
    SIGN_IN_COMPLETE = "SIGN_IN_COMPLETE",
    SIGN_IN_FAILED = "SIGN_IN_FAILED"
  }
}
