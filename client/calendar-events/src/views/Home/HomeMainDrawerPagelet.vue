<template>
  <div class="main-drawer-pagelet">
    <card-flat>
      <div class="container">
        <tabs-browser-panel :data-links="data" alignment="right"></tabs-browser-panel>
        <router-view></router-view>
      </div>
    </card-flat>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from "vue-property-decorator";
import TabsBrowserPanel, { DataLinkTabBrowser } from '@/components/Layouts/TabsBrowserPanel/TabsBrowserPanel.vue';
import CardFlat from '@/components/Cards/CardFlat.vue';
import linkRoutes from '@/constants/links-routes';

@Component({
  components: {
    TabsBrowserPanel,
    CardFlat
  },
})
export default class MainDrawerPagelet extends Vue {
  private data !: DataLinkTabBrowser[];
  created(){
    this.data = [
      {
      to : linkRoutes.home.children.default,
      text : "my events"
    },
          {
      to : linkRoutes.home.children.newEvent,
      text : "new event"
    },
    {
      to : "/s",
      text : "item 3"
    },
    {
      to : "/s",
      text : "item 4"
    }
    ];
  }
}
</script>

<style lang="scss" scoped>
.main-drawer-pagelet {
    width: 100%;
    padding: 1em 2em 0;
    .container {
      padding: 1em;
    }
}
</style>
