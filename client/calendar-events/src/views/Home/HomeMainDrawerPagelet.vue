<template>
  <div class="main-drawer-pagelet">
    <card-flat>
      <div class="container">
        <router-view></router-view>
      </div>
    </card-flat>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from "vue-property-decorator";
import {CardFlat} from "@/components/Common/Cards";

@Component({
  components: {
    CardFlat,
  },
})
export default class MainDrawerPagelet extends Vue {
  private datetime: Date = new Date();
}
</script>

<style lang="scss" scoped>
.main-drawer-pagelet {
  width: 100%;
  padding: 1em 2em;
  display: flex;
  align-items: stretch;
  > * {
    width: 100%;
  }
  .container {
    padding: 1em;
  }
}
</style>
