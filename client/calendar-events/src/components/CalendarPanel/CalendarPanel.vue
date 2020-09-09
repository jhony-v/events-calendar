<template>
  <div class="container-calendar">
    <div class="calendar-header">
      <calendar-header-navigator></calendar-header-navigator>
    </div>
    <div class="calendar-body">
      <calendar-weekdays></calendar-weekdays>
      <calendar-grid-all-dates-month></calendar-grid-all-dates-month>
    </div>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from "vue-property-decorator";
import CalendarHeaderNavigator from "./CalendarHeaderNavigator/CalendarHeaderNavigator.vue";
import CalendarGridAllDatesMonth from "./CalendarPreviewDatesOfMonth/CalendarGridAllDatesMonth.vue";
import CalendarWeekdays from "./CalendarWeekdays/CalendarWeekdays.vue";

@Component({
  components: {
    CalendarHeaderNavigator,
    CalendarGridAllDatesMonth,
    CalendarWeekdays,
  },
})
export default class CalendarPanelContainer extends Vue {}
</script>
<style lang="scss" scoped>
.container-calendar {
  background-color: var(--color-bg-primary);
  margin: auto;
  padding: 10px;
}
</style>
