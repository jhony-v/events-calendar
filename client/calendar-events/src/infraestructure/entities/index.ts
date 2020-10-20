export namespace UserNamespace {
  export interface User {
    email?: string;
    password?: string;
    fullName?: string;
    username?: string;
    description?: string;
  }

  export interface UserAuth {
    email?: string;
    password?: string;
  }

  export interface UserAuthResponse {
    token: string;
    validToken?: boolean;
    user: {
      email?: string;
      fullName?: string;
      username?: string;
      userId?: string;
    };
  }
}
