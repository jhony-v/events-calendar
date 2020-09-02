<template>
  <div class="grid-item">
    <slot></slot>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from "vue-property-decorator";

@Component({})
export default class CalendarItemGridDate extends Vue {}
</script>

<style lang="scss" scoped>
.grid-item {
  text-align: center;
  padding: 1em 5px;
  font-size: 13px;
}
</style>
