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
        text: "recientes",
      },
      {
        to: linkRoutes.home.children.newEvent,
        text: "agregar proyecto",
      },
      {
        to: linkRoutes.home.children.workers,
        text: "trabajadores",
      },
      {
        to: linkRoutes.home.children.allEvents,
        text: "proyectos",
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
    &::-webkit-scrollbar {
      width: 6px;
    }
    &::-webkit-scrollbar-thumb {
      border-radius: 6px;
      background: var(--color-scrollbar-thumb);
    }
  }
}
</style>
