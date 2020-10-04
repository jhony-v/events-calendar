<template>
  <div class="home-scenes">
    <div class="home-scenes__navigator">
      <tabs-browser-panel :data-links="data" alignment="right"></tabs-browser-panel>
    </div>
    <div class="home-scenes__preview">
      <router-view></router-view>
    </div>
  </div>
</template>
<script lang="ts">
import { Vue, Component } from "vue-property-decorator";
import TabsBrowserPanel, {DataLinkTabBrowser } from "@/components/Layouts/TabsBrowserPanel/TabsBrowserPanel.vue";
import linkRoutes from "@/constants/links-routes";

@Component({
  components: {
    TabsBrowserPanel,
  },
})
export default class HomeDefaultScene extends Vue {
  private data!: DataLinkTabBrowser[];
  created() {
    this.data = [
      {
        to: linkRoutes.home.children.default,
        text: "my events",
      },
      {
        to: linkRoutes.home.children.newEvent,
        text: "new event",
      },
      {
        to: "/s",
        text: "item 3",
      },
      {
        to: "/s",
        text: "item 4",
      },
    ];
  }
}
</script>
<style lang="scss" scoped>
.home-scenes {
  height: 100%;
  display: grid;
  grid-template-rows: min-content 1fr;
  &__preview {
    overflow-y: auto;
  }
}
</style>
