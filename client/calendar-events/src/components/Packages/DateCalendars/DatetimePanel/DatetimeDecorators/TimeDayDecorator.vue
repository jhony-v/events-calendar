<template>
  <div class="decorator">
    <span class="decorator__time">{{ computedGetTime }}</span>
    <span class="decorator__weekday">{{ computedGetWeekday }}</span>
  </div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from "vue-property-decorator";
import moment from "moment";

@Component({})
export default class TimeDayDecorator extends Vue {
  @Prop() datetime!: string;

  get computedGetTime() {
    return moment(this.datetime).format("HH:mm a");
  }

  get computedGetWeekday() {
    return moment(this.datetime).format("dddd");
  }
}
</script>

<style lang="scss" scoped>
.decorator {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  &__time {
    font-weight: 900;
    font-size: 2.5rem;
    color: var(--color-text-neutral-medium);
  }
  &__weekday {
  font-size: .9rem;
    color: var(--color-text-neutral);
    margin-top: 10px;
  }
}
</style>
