<template>
  <div class="grid-all-dates">
    <calendar-item-grid-date v-for="(value, key) in dates" :key="key">
      {{ value.date.date() }}
    </calendar-item-grid-date>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from "vue-property-decorator";
import moment from "moment";
import CalendarItemGridDate from "./CalendarItemGridDate.vue";
import CalendarPanelRepository, { CalendarCurrentDate } from "../Repositories/CalendarPanelRepository";

@Component({
  components: {
    CalendarItemGridDate,
  },
})
export default class CalendarGridAllDaysMonth extends Vue {
  private dates: CalendarCurrentDate[] = [];
  private calendarPanelRepository : CalendarPanelRepository = new CalendarPanelRepository();
  created() {
    this.dates = this.calendarPanelRepository.getAllDatesByMonth(moment("2020-09-01"));
  }
}


</script>

<style lang="scss" scoped>
.grid-all-dates {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
}
</style>
