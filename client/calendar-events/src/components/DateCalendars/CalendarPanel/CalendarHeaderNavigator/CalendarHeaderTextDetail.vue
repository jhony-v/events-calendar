<template>
  <div class="text-date">
    <span class="text-date--month">January</span>
    <span class="text-date--year">, 2020</span>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
.text-date {
  font-size: 1.8em;
  color: var(--color-text-neutral-darker);
  &--month {
    font-weight: bold;
  }
  &--year {
    letter-spacing: 2px;
  }
}
</style>
