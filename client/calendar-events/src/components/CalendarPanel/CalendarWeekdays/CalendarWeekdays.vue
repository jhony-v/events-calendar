<template>
  <div class="weekdays">
    <div v-for="(day, index) in weekdays" :key="index" class="weekdays__item">
      {{ day }}
    </div>
  </div>
</template>
<script lang="ts">
import { Vue, Component } from "vue-property-decorator";

@Component({})
export default class CalendarWeekDays extends Vue {
  private weekdays: string[] = [
    "Lun",
    "Mar",
    "Mie",
    "Jue",
    "Vie",
    "Sab",
    "Dom",
  ];
}
</script>

<style lang="scss" scoped>
.weekdays {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  &__item {
    text-align: center;
    padding: 1em 2px;
    font-weight: bold;
    user-select: none;
    color: var(--color-text-neutral-darker);
  }
}
</style>
