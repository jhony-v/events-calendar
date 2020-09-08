<template>
  <div class="pagelet">
    <div class="pagelet__navigator">
      <navigator-header-toolbar></navigator-header-toolbar>
    </div>
    <div class="pagelet__main">
        <calendar-panel></calendar-panel>
    </div>
  </div>
</template>

<script>
import LoadingSpinner from "@/components/Interface/LoadingSpinner.vue";
import CalendarPanel from "@/components/CalendarPanel/CalendarPanel.vue";
import NavigatorHeaderToolbar from "@/components/Layouts/NavigatorHeaderToolbar/NavigatorHeaderToolbar.vue";

export default {
  components : {
    LoadingSpinner,
    CalendarPanel,
    NavigatorHeaderToolbar,
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
