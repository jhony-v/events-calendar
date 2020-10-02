<template>
  <div class="wrapper-app">
    <div class="wrapper-app__title">Calendar Events</div>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from "vue-property-decorator";

@Component({})
export default class WrapperApplicationName extends Vue{}
</script>

<style lang="scss" scoped>
.wrapper-app {
  display: inline-block;
  &__title {
    font-weight: 900;
    font-size: 1.6rem;
    color: var(--color-text-neutral-darker);
  }
}
</style>
