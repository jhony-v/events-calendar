<template>
  <div class="scrollable">
    <div :class="computedClassScrollable"><slot></slot></div>
  </div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from "vue-property-decorator";

@Component({})
export default class FlatListScrollableDirectionController extends Vue {
  @Prop() isHorizontal!: boolean;
  get computedClassScrollable() {
    return ["flat-list", this.isHorizontal ? "flat-list__horizontal" : ""];
  }
}
</script>

<style lang="scss" scoped>
.scrollable {
  width: calc(100vw - calc(300px + 8em));
}
.flat-list {
    &__horizontal {
    overflow-x: auto;
    display: flex;
    &::-webkit-scrollbar{
      display:none;
    }
    > * {
      flex: none;
    }
  }
}
</style>
