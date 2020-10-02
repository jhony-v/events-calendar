<template>
  <div class="logout">
    Logout
  </div>
</template>

<script lang="ts">
import { Vue, Component } from "vue-property-decorator";
import {TextLabel} from "@/components/Common/TextLabels";

@Component({
  components: {
    TextLabel,
  },
})
export default class ButtonLogoutLink extends Vue {}
</script>

<style lang="scss" scoped>
.logout {
  text-align: center;
  margin: auto;
  color: var(--color-text-neutral);
  font-weight: 900;
}
</style>
