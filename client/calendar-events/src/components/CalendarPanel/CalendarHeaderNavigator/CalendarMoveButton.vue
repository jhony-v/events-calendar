<template>
  <div class="button-move">
    <i class="material-icons">{{ icon }}</i>
  </div>
</template>

<script lang="ts">
import { Vue, Prop, Component } from "vue-property-decorator";

@Component({})
export default class CalendarMoveButton extends Vue {
  @Prop() icon!: string;
}
</script>

<style lang="scss" scoped>
@mixin size($size) {
  width: $size;
  height: $size;
}
.button-move {
    @include size(30px);
    background-color: var(--color-border-neutral);
    color: var(--color-text-neutral-medium);
    border-radius: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: .1s;
    &:hover{
        transform: scale(1.2);
    }
}
</style>
