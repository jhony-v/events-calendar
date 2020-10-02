<template>
  <div class="pagelet">
    <div class="pagelet__navigator">
      <navigator-header-toolbar></navigator-header-toolbar>
    </div>
    <div class="pagelet__main">
      <home-aside-pagelet></home-aside-pagelet>
      <home-main-drawer-pagelet></home-main-drawer-pagelet>
    </div>
  </div>
</template>

<script>
import {LoadingSpinner} from "@/components/Common/Loaders";
import NavigatorHeaderToolbar from "@/components/Layouts/NavigatorHeaderToolbar/NavigatorHeaderToolbar.vue";
import HomeAsidePagelet from "./HomeAsidePagelet.vue";
import HomeMainDrawerPagelet from "./HomeMainDrawerPagelet.vue";

export default {
  components: {
    HomeAsidePagelet,
    HomeMainDrawerPagelet,
    LoadingSpinner,
    NavigatorHeaderToolbar,
  },
};
</script>

<style lang="scss" scoped>
.pagelet {
  height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: stretch;
  &__navigator {
    position: relative;
    z-index: 10;
  }
  &__main {
    height: 100%;
    display: flex;
    align-items: stretch;
    overflow-y: hidden;
  }
}
</style>
