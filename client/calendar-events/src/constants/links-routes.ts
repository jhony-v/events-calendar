const linkRoutes = {
  home: {
    default: "/",
    children: {
      default: "/",
      newEvent: "/new-event",
      workers : "/workers",
      allEvents : "/all-events",
    },
  },
  about: {
    default: "/about",
  },
  explore: {
    default: "/explore",
  },
  settings: {
    default: "/settings",
    children: {
      default: "/",
    },
  },
  profile: {
    default: "/profile",
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
