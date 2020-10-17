<template>
  <div :class="['flex', alignment]">
    <slot></slot>
  </div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from "vue-property-decorator";
@Component({})
export default class ContainerWrapper extends Vue {
  @Prop() alignment!: string;
}
</script>

<style lang="scss" scoped>
.flex {
  display: flex;
}
$wrapperAlignment: left flex-start, center center, right flex-end;
@each $alignment, $justify in $wrapperAlignment {
  .#{$alignment} {
    justify-content: $justify;
  }
}
</style>
