<template>
  <div class="options-user">
    <div class="options-user__buttons">
        <button-rounded-iconify class="buttons--options" type="add"></button-rounded-iconify>
        <button-rounded-iconify class="buttons--options" type="notification"></button-rounded-iconify>
    </div>
    <chip-avatar-user-informational
      image="https://cdn.pixabay.com/photo/2018/12/01/00/10/blue-hour-3848856__340.jpg"
      username="Mark Lenderset Tormk"
      detail="userask@gmail.com"
      class="navigator__user"
    ></chip-avatar-user-informational>
  </div>
</template>

<script lang="ts">
import { Vue,Component } from "vue-property-decorator"
import { ButtonRoundedIconify } from "@/components/Common/Buttons";
import { ChipAvatarUserInformational } from "@/components/Common/Chips";

@Component({
    components: {
        ButtonRoundedIconify,
        ChipAvatarUserInformational,
    }
})
export default class OptionsUser extends Vue {

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