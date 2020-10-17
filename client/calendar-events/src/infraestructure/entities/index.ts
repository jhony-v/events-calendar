import { namespace } from "vuex-class";

export namespace UserNamespace {
  export interface UserAuth {
    email?: string;
    password?: string;
    username?: string;
  }
  export interface User extends UserAuth {
    fullName?: string;
    description?: string;
  }
}
