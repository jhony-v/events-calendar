<template>
  <div class="pagelet">
    <div class="pagelet__navigator">
      <navigator-header-toolbar></navigator-header-toolbar>
    </div>
    <div class="pagelet__main">
    </div>
  </div>
</template>

<script>
import LoadingSpinner from "@/components/styled/LoadingSpinner.vue";

export default {
  components : {
    LoadingSpinner,
    NavigatorHeaderToolbar : () => ({
      component : import("@/components/layouts/NavigatorHeaderToolbar/NavigatorHeaderToolbar.vue"),
      loading : LoadingSpinner
    })
  }
}
</script>

<style lang="scss" scoped>
.pagelet {
  height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: stretch;
  &__navigator {
    height: 60px;
    position: relative;
    z-index: 10;
  }
  &__main {
    height: 100%;
    overflow-y: auto;
  }
}
</style>
