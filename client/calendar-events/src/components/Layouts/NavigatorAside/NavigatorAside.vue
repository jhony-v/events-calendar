<template>
  <div class="navigator-aside">
    <div
      v-for="(value, index) in listNavLinks"
      :key="index"
      class="navigator-aside__item"
    >
      <button-rounded-link :to="value.link" :text="value.text">{{
        value.icon
      }}</button-rounded-link>
    </div>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from "vue-property-decorator";
import { ButtonRoundedLink } from "@/components/Common/Buttons";
import linkRoutes from "@/constants/links-routes";

interface INavLink {
  link: string;
  icon: string;
  text: string;
}

const dataListNavLinks: INavLink[] = [
  {
    link: linkRoutes.home.default,
    icon: "home",
    text: "inicio",
  },
  {
    link: linkRoutes.about.default,
    icon: "people",
    text: "acerca de mí",
  },
  {
    link: linkRoutes.explore.default,
    icon: "explore",
    text: "explorar",
  },
  {
    link: linkRoutes.settings.default,
    icon: "settings",
    text: "configuración",
  },
];

@Component({
  components: {
    ButtonRoundedLink,
  },
})
export default class NavigatorAside extends Vue {
  listNavLinks: INavLink[] = dataListNavLinks;
}
</script>

<style lang="scss" scoped>
.navigator-aside {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-top: 2em;
  &__item {
    margin-bottom: 2em;
  }
}
</style>
