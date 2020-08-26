<template>
  <div class="loading-container">
    <div class="spinner"></div>
    <span class="label" v-if="label">{{ label }}</span>
  </div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from "vue-property-decorator";

@Component({})
export default class LoadingSpinner extends Vue {
  @Prop() label!: string;
}
</script>

<style lang="scss" scoped>
$size: 30px;
.loading-container {
  text-align: center;
}
.spinner {
  width: $size;
  height: $size;
  border-radius: 100%;
  border: 3px solid transparent;
  border-left-color: var(--color-primary);
  border-bottom-color: var(--color-primary);
  animation: loading 450ms infinite linear;
  margin: auto;
  @keyframes loading {
    from {
      transform: rotate(-1turn);
    }
  }
}
.label {
  color: var(--color-text-neutral);
  font-size: 13px;
  text-align: center;
  margin-top: 15px;
  display: block;
  font-weight: bold;
}
</style>
