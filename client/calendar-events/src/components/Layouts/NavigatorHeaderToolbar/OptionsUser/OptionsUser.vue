<template>
  <div class="options-user">

    <!-- user options with actions -->
    <div class="options-user__buttons">
        <button-rounded-iconify class="buttons--options" type="add" @click="toggleModal()"></button-rounded-iconify>
        <button-rounded-iconify class="buttons--options" type="notification" @click="toggleModal()"></button-rounded-iconify>
    </div>
    <chip-avatar-user-informational
      image="https://cdn.pixabay.com/photo/2018/12/01/00/10/blue-hour-3848856__340.jpg"
      username="Jhony Vega"
      detail="jhony.vega@gmail.com"
      class="navigator__user"
    ></chip-avatar-user-informational>

    
    <!-- preview modal of actions user -->
    <modal-full-screen title="New management" :open="openModal" @onclose="toggleModal()"></modal-full-screen>

  </div>
</template>

<script lang="ts">
import { Vue,Component } from "vue-property-decorator"
import { ButtonRoundedIconify } from "@/components/Common/Buttons";
import { ChipAvatarUserInformational } from "@/components/Common/Chips";
import { ModalFullScreen } from '@/components/Common/Modals';

@Component({
    components: {
        ButtonRoundedIconify,
        ChipAvatarUserInformational,
        ModalFullScreen,
    }
})
export default class OptionsUser extends Vue {
  private openModal : boolean = false;
  toggleModal(){
    this.openModal  = !this.openModal;
  }
}
</script>

<style lang="scss" scoped>
.options-user {
    display: flex;
    margin-left: auto;
    align-items: center;
    $buttons: buttons;
    &__buttons {
        display: flex;
        margin: 0 20px;
        .#{$buttons}--options {
            margin: 0 10px;
        }
    }
}
</style>