<template>
  <div class="main-drawer-pagelet">
    <card-flat class="container">
      <router-view></router-view>
    </card-flat>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from "vue-property-decorator";
import { CardFlat } from "@/components/Common/Cards";
import { FlatListScrollableDirectionController } from "@/components/Common/Scrollables";

@Component({
  components: {
    CardFlat,
    FlatListScrollableDirectionController,
  },
})
export default class MainDrawerPagelet extends Vue {
  private datetime: Date = new Date();
}
</script>

<style lang="scss" scoped>
.main-drawer-pagelet {
  width: 100%;
  padding: 1em 2em 1em 0;
  display: flex;
  align-items: stretch;
  .container {
    width: 100%;
    padding: 1em;
    overflow-y: scroll;
    border-top-right-radius: 5px;
    border-bottom-right-radius: 5px;
    &::-webkit-scrollbar {
      width: 6px;
    }
    &::-webkit-scrollbar-thumb {
      background: var(--color-scrollbar-thumb);
      border-radius: 20px;
    }
  }
}
</style>
