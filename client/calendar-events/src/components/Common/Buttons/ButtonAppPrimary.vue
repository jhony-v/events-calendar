<template>
  <button class="button-primary">
    <slot></slot>
  </button>
</template>

<script>
export default {};
</script>

<style lang="scss">
.button-primary {
    background-color: var(--color-primary);
    border-radius: 10px;
    padding: 13px 25px;
    color: white;
    font-weight: bold;
    display: inline-block;
}
</style>