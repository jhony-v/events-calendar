<template>
  <portal to="app-modal" :disabled="open">
    <div class="modal__backdrop">
      <card-flat class="modal__container">
        <div class="modal__container--header">
          <text-label :weight="true">{{title}}</text-label>
          <button-rounded-iconify type="close" class="close-button" @click="onClose" ></button-rounded-iconify>
        </div>
        <div class="modal__container--body"><slot></slot></div>
      </card-flat>
    </div>
  </portal>
</template>

<script lang="ts">
import { Vue, Component, Prop, Watch } from "vue-property-decorator";
import { CardFlat } from "../Cards";
import { ButtonRoundedIconify } from "@/components/Common/Buttons";
import { TextLabel } from '../TextLabels';


@Component({
  components: {
    CardFlat,
    ButtonRoundedIconify,
    TextLabel
  },
})
export default class ModalFullScreen extends Vue {
  @Prop() title !: string;
  @Prop({ default: false }) open!: boolean;

  onClose() {
    this.$emit("onclose");
  }
}
</script>

<style lang="scss" scoped>
.modal {
  &__backdrop {
    background: var(--color-backdrop);
    position: fixed;
    top: 0;
    left: 0;
    bottom: 0;
    right: 0;
    z-index: 1000;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  &__container {
    width: 600px;
    padding: 20px;
    &--header {
      display: flex;
      align-items: flex-start;
      .close-button {
        margin-left: auto;
      }
    }
    &--body {
      padding-top: 20px;
      padding-bottom: 20px;
    }
  }
}
</style>
