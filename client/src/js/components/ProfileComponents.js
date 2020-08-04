Vue.component("profile-description-smooth", {
  props: ["text"],
  template: `<p class="profile__text--smooth">{{text}}</p>`,
});

Vue.component("profile-wrapper-puntuation", {
  props: ["text", "points"],
  template: `
    <div class="profile-panel--flex flex-align-center">
        <div class="profile__text--dark--medium">{{points}}</div>
        <div class="profile__text--smooth child">{{text}}</div>
    </div>
    `,
});

Vue.component("profile-avatar",{
  props : ["image","styles"],
  template : `
    <img :src="image" :style="styles" alt="" class="profile-panel__image" />
  `
})


Vue.component("profile-tab-controller",{
  props : ["active","text"],
  template : `
    <div :class="{
      'profile-tab-controller' : true,
      'profile-tab-controller--active' : active
    }" @click="onClickTab">{{text}}</div>
  `,
  methods : {
    onClickTab(e) {
      this.$emit("onclick",e);
    }
  }
})