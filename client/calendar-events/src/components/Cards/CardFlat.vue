<template>
  <div class="card-flat"><slot></slot></div>
</template>

<script lang="ts">
import { Vue, Component } from "vue-property-decorator";
@Component({})
export default class CardFlat extends Vue {}
</script>

<style lang="scss" scoped>
.card-flat {
  background-color: var(--color-layout-primary);
  border-radius: 25px;
}
</style>
