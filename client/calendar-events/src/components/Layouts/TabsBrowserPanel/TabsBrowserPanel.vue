<template>
  <div :class="computedTabBrowserClassNames">
    <tab-link v-for="(item, index) in dataLinks" :key="index" :to="item.to">
      {{ item.text }}
    </tab-link>
  </div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from "vue-property-decorator";
import TabLink from "./TabLink.vue";

export interface DataLinkTabBrowser {
  to?: string;
  text?: string;
}

@Component({
  components: {
    TabLink,
  },
})
export default class TabsBrowserPanel extends Vue {
  @Prop() dataLinks!: DataLinkTabBrowser[];
  @Prop() alignment!: string;
  get computedTabBrowserClassNames() {
    return ["tab-browser", this.alignment];
  }
}
</script>

<style lang="scss" scoped>
.tab-browser{
  display: inline-block;
  width: 50%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  &.center {
    margin: auto;
  }
  &.left {
    margin-right: auto;
  }
  &.right {
    margin-left: auto;
  }
}
</style>
