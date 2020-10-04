<template>
  <button class="button"><slot></slot></button>
</template>

<script lang="ts">
import { Vue, Component } from "vue-property-decorator";

@Component({})
export default class ButtonDefault extends Vue {

}
</script>

<style lang="scss" scoped>
.button {
    font-weight: bold;
    padding: 12px 40px;
    border-radius: 10px;
    background-color: rgba(0,0,0,.05);
}
</style>