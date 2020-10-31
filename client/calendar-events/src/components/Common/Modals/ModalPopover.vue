<template>
  <div class="popover">
    <div class="popover__button" @click="onOpenList">
      <slot name="button"></slot>
    </div>
    <card-flat class="popover__list" v-if="open">
      <slot name="list"></slot>
    </card-flat>
  </div>
</template>
<script lang="ts">
import { Vue, Component } from "vue-property-decorator";
import { CardFlat } from "../Cards";

@Component({
  components: {
    CardFlat,
  },
})
export default class ModalPopover extends Vue {
  private open: boolean = false;

  onOpenList() {
    this.open = !this.open;
  }

  onCloseList() {
    this.open = false;
  }
}
</script>

<style lang="scss" scoped>
.popover {
  position: relative;
  &__button {
    display: inline-block;
  }
  &__list {
    position: absolute;
    transform: translate(-80%,0);
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
    border-width: 0;
  }
}
</style>
