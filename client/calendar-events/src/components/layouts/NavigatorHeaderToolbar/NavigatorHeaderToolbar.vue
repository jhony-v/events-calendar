<template>
  <div class="navigator">
    <wrapper-application-name></wrapper-application-name>
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Fuga earum, ab qui
    labore dolore libero inventore autem itaque at repudiandae quo dolorum
    similique quis deleniti cupiditate, atque nostrum veniam. Cumque.
  </div>
</template>

<script lang="ts">
import { Vue, Component } from "vue-property-decorator";
import WrapperApplicationName from "@/components/GeneralApplication/WrapperApplicationName.vue";

@Component({
  components: {
    WrapperApplicationName,
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
