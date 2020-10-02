<template>
  <div class="navigator">
    <wrapper-application-name></wrapper-application-name>
    <options-navigate></options-navigate>
    <chip-avatar-user-informational
      image="https://cdn.pixabay.com/photo/2018/12/01/00/10/blue-hour-3848856__340.jpg"
      username="Mark Lenderset Tormk"
      detail="userask@gmail.com"
    ></chip-avatar-user-informational>
  </div>
</template>
<script lang="ts">
import { Vue, Component } from "vue-property-decorator";
import { ChipAvatarUserInformational } from "@/components/Common/Chips";
import OptionsNavigate from "./OptionsNavigate/OptionsNavigate.vue";
import WrapperApplicationName from "@/components/Packages/GeneralApplication/WrapperApplicationName.vue";

@Component({
  components: {
    WrapperApplicationName,
    ChipAvatarUserInformational,
    OptionsNavigate
  },
})
export default class NavigatorHeadertoolbar extends Vue {}
</script>

<style lang="scss" scoped>
.navigator {
  background: var(--color-bg-page);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1em 2em;
}
</style>
