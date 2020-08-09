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
  color: rgb(90, 90, 90);
  font-size: 1.2em;
  @extend %auth-form-block;
  &--master {
    margin-bottom: 3em;
    display: flex;
    align-items: center;
    justify-content: center;
    .material-icons {
      color: rgb(30, 190, 230);
      font-size: 2em;
    }
  }
}
</style>
