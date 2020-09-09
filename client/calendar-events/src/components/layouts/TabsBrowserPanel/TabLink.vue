<template>
  <router-link class="tab-link" active-class="tab-link--active" :to="to">
    <slot></slot>
  </router-link>
</template>

<script lang="ts">
import { Vue, Component, Prop } from "vue-property-decorator";

@Component({})
export default class TabLink extends Vue {
  @Prop() to!: string;
}
</script>

<style lang="scss" scoped>
.tab-link {
  display: inline-block;
  color: var(--color-text-neutral);
  font-weight: bold;
  padding: 10px;
  font-size: .9rem;
  &--active {
      color: var(--color-primary);
  }
}
</style>
