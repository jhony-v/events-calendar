<template>
  <div class="wrapper">
      <div class="wrapper__subtitle">
      <text-label  :weight="true" fontSizeText="small">{{label}}</text-label>
      </div>
    <input class="input-field__outline" :placeholder="placeholder" v-if="type == 'input'" :type="checkIsPassword" />
    <textarea class="input-field__outline" :placeholder="placeholder" v-else-if="type == 'textarea'" />
  </div>
</template>

<script lang="ts">
import { TextLabel } from "@/components/Common/TextLabels";
import { Vue, Component, Prop } from "vue-property-decorator";
@Component({
    components : {
        TextLabel
    }
})
export default class extends Vue {
  @Prop() type!: string;
  @Prop() placeholder!: string;
  @Prop() label!: string;
  @Prop() isPassword!: boolean;

  get checkIsPassword() {
    return this.isPassword ? "password" : "text";
  }
}
</script>

<style lang="scss" scoped>
.wrapper {
  &__subtitle {
      margin-bottom: 6px;
  }
  .input-field__outline {
    border: 1px solid var(--color-text-neutral);
    border-radius: 15px;
    padding: 10px;
    width: 100%;
    resize: none;
  }
}
</style>