<template>
  <div class="auth-form__options">
    <div class="auth-form__options__google">
      <img
        src="https://image.flaticon.com/teams/slug/google.jpg"
        width="30px"
      />
      Sign in with Google
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
.auth-form__options {
  background: rgba(0, 0, 0, 0.03);
  padding: 2em;
  margin: -3em;
  margin-top: 2em;
  text-align: center;
  &__google {
    display: inline-flex;
    align-items: center;
    font-weight: bold;
    font-size: 14px;
    color: rgb(90, 90, 90);
    cursor: pointer;
  }
}
</style>
