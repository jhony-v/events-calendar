<template>
  <div class="navigator">
    <wrapper-application-name></wrapper-application-name>
    <options-navigate></options-navigate>
    <options-user></options-user>
  </div>
</template>
<script lang="ts">
import { Vue, Component } from "vue-property-decorator";
import OptionsNavigate from "./OptionsNavigate/OptionsNavigate.vue";
import WrapperApplicationName from "@/components/Packages/GeneralApplication/WrapperApplicationName.vue";
import OptionsUser from "./OptionsUser/OptionsUser.vue";

@Component({
  components: {
    WrapperApplicationName,
    OptionsNavigate,
    OptionsUser
  },
})
export default class NavigatorHeadertoolbar extends Vue {}
</script>

<style lang="scss" scoped>
.navigator {
  background: var(--color-bg-page);
  display: flex;
  align-items: center;
  padding: 1em 2em;
}
</style>
