Vue.component("link-navigator", {
  props : ["text","icon","link"],
  data : () => ({
    currentLink : "",
  }),
  template: `
    <div class="navigator-item">
        <a :href="link" :class="{'item-link':true,'item-link--active':activeCurrentLink}"> 
          <i class="material-icons">{{icon}}</i> {{text}}
        </a>
    </div>
  `,
  computed : {
    activeCurrentLink() {
      return this.currentLink === window.location.pathname;
    }
  },
  created(){
    this.currentLink = this.link;
  }
});
