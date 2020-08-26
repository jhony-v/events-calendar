<template>
  <div class="form-header">
    <div class="auth-form__title--master auth-form__title">
      CALENDAR <i class="material-icons">emoji_events</i> EVENTS
    </div>
    <h3 class="auth-form__title">LOGIN</h3>
  </div>
</template>

<style lang="scss" scoped>
%auth-form-block {
  text-align: center;
  display: block;
  font-weight: bold;
  margin-bottom: 2em;
}
.auth-form__title {
  color: var(--color-text-neutral-medium);
  font-size: 1.2em;
  @extend %auth-form-block;
  &--master {
    margin-bottom: 3em;
    display: flex;
    align-items: center;
    justify-content: center;
    .material-icons {
      color: var(--color-primary);
      font-size: 2em;
    }
  }
}
</style>
