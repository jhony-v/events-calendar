<template>
  <div class="field">
    <label class="field__label">{{label}}</label>
    <input class="field__input" spellcheck="false" :ref="input" @input="onChangeInput" />
  </div>
</template>

<script>
import { Vue, Component, Prop, Emit, Ref } from "vue-property-decorator";

@Component({})
export default class InputField extends Vue {
  @Prop() label;
  @Ref() input;
  onChangeInput = (e) => this.$emit("oninput",e.target.value);
}
</script>

<style lang="scss" scoped>
.field {
  display: flex;
  flex-direction: column;
  width: 100%;
  margin: auto;

  &__input {
    border: 1px solid var(--color-border-neutral);
    border-radius: 20px;
    padding: 10px;
    text-align: center;
    font-weight: bold;
    font-size: 13px;
    background: none;
    color: var(--color-text-neutral-darker);
  }
  &__label {
    text-align: center;
    font-size: 14px;
    color: var(--color-text-neutral);
    text-shadow: 0 5px 10px var(--color-border-neutral);
    margin-bottom: 10px;
    font-weight: bold;
  }
}
</style>
