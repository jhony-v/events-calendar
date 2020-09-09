<template>
  <div class="logout">
  </div>
</template>

<script lang="ts">
import { Vue, Component } from "vue-property-decorator";
import TextLabel from "../Interface/TextLabel.vue";

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
}
</style>
