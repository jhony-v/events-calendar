import "./components/LinkNavigator.js";
import "./components/ProfileComponents.js";

const initialState = {
  tabs: [
    { name : "Publicaciones",key:1,component :"viewPublications",},
    { name : "Eventos Seguidos",key:2,component :"viewFollowers",},
  ],
  currentTab : {
    key : 1
  }
};

const ACTIONS = {
  SELECT_TAB: "SELECT_TAB",
};

const store = new Vuex.Store({
  state: initialState,
  mutations : {
    [ACTIONS.SELECT_TAB] : (state,payload) => {
      state.currentTab = payload;
    } 
  },
  actions : {
    selectCurrentTab : ({commit},tab) => {
      commit(ACTIONS.SELECT_TAB,tab)
    } 
  }
});

new Vue({
  el: "#app",
  store,
  methods : {
    ...Vuex.mapActions({
      selectCurrentTab : 'selectCurrentTab'
    })
  },
  computed : {
    ...Vuex.mapState({
      allTabs : state => state.tabs,
      currentTabKey : state => state.currentTab.key
    })
  },
});
