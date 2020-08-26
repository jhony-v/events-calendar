import router from ".";

router.beforeEach((to,from,next) => {
  if(to.matched.some(record => record.meta.auth)) {
    const logged = true;
    if(logged) {
      next();
    }
    else {
      next({
        path : "/sign-in"
      })
    }
  }
  else {
    next();
  }
})