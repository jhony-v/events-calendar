<template>
  <span :class="computedClassNameUIText"><slot></slot></span>
</template>

<script lang="ts">
import { Vue, Component, Prop } from "vue-property-decorator";

@Component({})
export default class TextLabel extends Vue {
  @Prop() weight!: boolean;
  @Prop() variant!: string;
  @Prop() fontSizeText!: string;
  get computedClassNameUIText() {
    return [
      "ui-text",
      this.variant,
      this.fontSizeText,
      {
        weight: this.weight,
      },
    ];
  }
}
</script>

<style lang="scss" scoped>
$sizes: (small 13px) (normal 0.95rem) (medium 1.15rem) (big 1.5rem);

.ui-text {
  &.weight {
    font-weight: 800;
  }
  &.smooth {
    color: var(--color-text-neutral-medium);
  }
  @each $className,$size in $sizes {
    &.#{$className} {
      font-size:$size;
    }
  }
}
</style>
