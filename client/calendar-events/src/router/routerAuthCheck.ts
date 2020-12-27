import store from '@/store';
import router from ".";

router.beforeEach((to,_,next) => {
  if(to.matched.some(record => record.meta.auth)) {
    const isAuthentication = store.getters["auth/isAuthentication"];
    if(true) {
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