<template>
  <div class="datetime-panel">
    <div class="datetime__calendar">
      <year-month-decorator></year-month-decorator>
      <time-day-decorator></time-day-decorator>
    </div>
    <div class="datetime__description">
      <text-label :weight="true"></text-label>
      <text-label variant="smooth"></text-label>
    </div>
    <div class="datetime__images">
      <task-multiple-chain-images></task-multiple-chain-images>
    </div>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from "vue-property-decorator";
import TextLabel from "@/components/Interface/TextLabel.vue";
import TaskMultipleChainImages from "@/components/TaskImages/TaskMultipleChainImages.vue";
import TimeDayDecorator from "./DatetimeDecorators/TimeDayDecorator.vue";
import YearMonthDecorator from "./DatetimeDecorators/YearMonthDecorator.vue";

@Component({
  components: {
    TextLabel,
    TaskMultipleChainImages,
    YearMonthDecorator,
    TimeDayDecorator,
  },
})
export default class DatetimePanel extends Vue {}
</script>

<style lang="scss" scoped>
.datetime-panel {
    background: var(--color-layout-primary);
    $datetime : datetime;
    &__calendar {
      display: flex;
      justify-content: space-between;
      padding-bottom: 1em;
    }
    &__description {
      padding: 10px 0;
    }
    &__images { 
      padding: 20px 0;
    }
}
</style>
