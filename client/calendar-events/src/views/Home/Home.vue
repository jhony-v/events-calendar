<template>
  <div class="pagelet">
    <div class="pagelet__navigator">
      <navigator-header-toolbar></navigator-header-toolbar>
    </div>
    <div class="pagelet__main">
        <calendar-panel>
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Aspernatur dolorem atque expedita placeat alias corrupti quas recusandae. Pariatur tempora reiciendis a odit, earum labore vero voluptas, quas animi quasi vel.
        </calendar-panel>
    </div>
  </div>
</template>

<script>
import LoadingSpinner from "@/components/Interface/LoadingSpinner.vue";
import CalendarPanel from "@/components/CalendarPanel/CalendarPanel.vue";

export default {
  components : {
    LoadingSpinner,
    CalendarPanel,
    NavigatorHeaderToolbar : () => ({
      component : import("@/components/Layouts/NavigatorHeaderToolbar/NavigatorHeaderToolbar.vue"),
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
