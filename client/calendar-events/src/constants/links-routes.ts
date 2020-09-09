const linkRoutes = {
  home: {
    default: "/",
    children: {
      default: "/",
      newEvent: "/new-event",
    },
  },
  about: {
    default: "/about",
  },
  explore : {
    default : "/explore"
  },
  settings: {
    default: "settings",
    children: {
      default: "/",
    },
  },
  forgotPassword: {
    default: "/forgot-password",
  },
  signIn: {
    default: "/sign-in",
  },
  error: {
    default: "*",
  },
};

export default linkRoutes;
