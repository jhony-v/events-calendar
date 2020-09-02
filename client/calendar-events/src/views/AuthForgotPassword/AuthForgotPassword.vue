<template>
  <div class="forgot">
    <div class="forgot--card">
      <div class="forgot__title">
        Did you forget your password?
      </div>
      <div class="forgot__message">
        Complete the fields to reset your password
      </div>
      <div class="forgot__body">
        <div class="forgot__control">
          <input-field label="Type your username"></input-field>
        </div>
        <div class="forgot__control">
          <input-field label="Type your email"></input-field>
        </div>
        <div class="forgot__control--right">
          <button class="forgot__button--reset">Reset password</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from "vue-property-decorator";
import InputField from "@/components/Interface/InputField.vue";

@Component({
  components: {
    InputField,
  },
})
export default class AuthForgotPassword extends Vue {}
</script>

<style lang="scss" scoped>
.forgot {
  &--card {
    margin: 1in auto;
    width: 400px;
    box-shadow: 0 10px 20px var(--color-border-neutral);
    border-radius: 10px;
    padding: 2em;
  }
  &__title {
    font-weight: bold;
    width: 80%;
    text-align: center;
    margin: auto;
    font-size: 1.6rem;
    margin-bottom: 15px;
    color: var(--color-text-neutral-darker);
  }
  &__message {
    color: var(--color-text-neutral);
    font-size: 0.8rem;
    margin: auto;
    text-align: center;
  }
  &__body {
    margin-top: 3em;
  }
  &__control {
    padding: 1em 0;
    &--right {
      text-align: right;
    }
  }
  &__button--reset {
    padding: 1em;
    color: var(--color-text-primary-light);
    background-color: var(--color-primary);
    margin-left: auto;
    border-radius: 10px;
    margin-top: 1em;
  }
}
</style>
