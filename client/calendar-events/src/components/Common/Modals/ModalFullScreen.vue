<template>
  <Portal target=".app-modals">
    <div class="modal__backdrop">
      <card-flat class="modal__container">
        <div class="modal__container--header">
          <button-rounded-iconify type="close" class="close-button"></button-rounded-iconify>
        </div>
        <div class="modal__container--body">
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Culpa, cum
          repellendus provident quo obcaecati vero aspernatur minus. Quisquam
          odio magnam est deleniti cupiditate. Numquam aperiam asperiores
          nesciunt fuga sapiente? Temporibus?
        </div>
      </card-flat>
    </div>
  </Portal>
</template>

<script lang="ts">
import { Vue, Component } from "vue-property-decorator";
import { CardFlat } from "../Cards";
import { ButtonRoundedIconify } from "@/components/Common/Buttons";

@Component({
  components: {
    CardFlat,
    ButtonRoundedIconify,
  },
})
export default class ModalFullScreen extends Vue {}
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
