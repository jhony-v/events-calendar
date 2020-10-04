<template>
  <div :class="['flat-list',computedGetDirHorizontal]">
    <div v-for="(item,index) in items" :key="index" class="flat-list__item">
        <slot name="item" :item="item"></slot>
    </div>
  </div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from "vue-property-decorator";

@Component({})
export default class FlatListScrollable extends Vue {
  @Prop() items!: any[];
  @Prop() direccionHorizontal !: boolean;

  get computedGetDirHorizontal() {
    return this.direccionHorizontal && 'flat-list__horizontal';
  }

}
</script>

<style lang="scss" scoped>
.flat-list {
    overflow-y: auto;

}
</style>
