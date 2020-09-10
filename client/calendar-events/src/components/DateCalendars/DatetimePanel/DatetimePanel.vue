<template>
  <div class="datetime-panel">
    <div class="datetime__calendar">
      <year-month-decorator :datetime="datetime"></year-month-decorator>
      <time-day-decorator :datetime="datetime"></time-day-decorator>
    </div>
    <div class="datetime__description">
      <text-label :weight="true">{{ title }}</text-label>
      <text-label variant="smooth" fontSizeText="small">{{ description }}</text-label>
      <slot name="description"></slot>
    </div>
    <div class="datetime__images">
      <task-multiple-chain-images :images="images"></task-multiple-chain-images>
      <slot></slot>
    </div>
  </div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from "vue-property-decorator";
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
export default class DatetimePanel extends Vue {
  @Prop() datetime!: string;
  @Prop() title!: string;
  @Prop() description!: string;
  @Prop() images !: string[];
}
</script>

<style lang="scss" scoped>
.datetime-panel {
  background: var(--color-layout-primary);
  padding: 30px;
  border-radius: 25px;
  $datetime: datetime;
  .#{$datetime}__calendar {
    display: flex;
    justify-content: space-between;
    padding-bottom: 1em;
  }
  .#{$datetime}__description {
    padding: 10px 0;
    display: flex;
    flex-direction: column;
    margin-top: 1em;
    > *:last-child {
      margin-top: 12px;
    }
  }
  .#{$datetime}__images {
    padding: 20px 0;
  }
}
</style>
