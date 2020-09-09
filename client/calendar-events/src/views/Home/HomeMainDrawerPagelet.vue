<template>
  <div class="main-drawer-pagelet">
    <calendar-panel></calendar-panel>
  </div>
</template>

<script>
import { Vue, Component } from "vue-property-decorator";
import CalendarPanel from "@/components/CalendarPanel/CalendarPanel.vue";

@Component({
  components: {
    CalendarPanel,
  },
})
export default class MainDrawerPagelet extends Vue {}
</script>

<style lang="scss" scoped>
.main-drawer-pagelet {
    width: 100%;
    padding: 1em 0 0;
}
</style>
