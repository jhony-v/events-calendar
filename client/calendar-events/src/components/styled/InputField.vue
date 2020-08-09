<template>
  <div class="field">
    <label class="field__label">{{label}}</label>
    <input class="field__input" spellcheck="false" />
  </div>
</template>

<script>
import { Vue, Component, Prop } from "vue-property-decorator";

@Component({})
export default class InputField extends Vue {
  @Prop() label;
}
</script>

<style lang="scss" scoped>
.field {
  display: flex;
  flex-direction: column;
  width: 100%;
  margin: auto;

  &__input {
    border: 1px solid rgba(0,0,0,.1);
    border-radius: 20px;
    padding: 10px;
    text-align: center;
    font-weight: bold;
    font-size: 13px;
    color: rgb(60,60,60);
  }
  &__label {
    text-align: center;
    font-size: 14px;
    color: rgb(187, 187, 187);
    text-shadow: 0 5px 10px rgba(0,0,0,.1);
    margin-bottom: 10px;
    font-weight: bold;
  }
}
</style>
