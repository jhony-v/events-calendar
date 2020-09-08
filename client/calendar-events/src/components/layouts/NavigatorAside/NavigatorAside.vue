<template>
  <div class="navigator-aside">
    <div v-for="(value, index) in listNavLinks" :key="index" class="navigator-aside__item">
        <button-rounded-link :to="value.link" :text="value.icon">{{value.icon}}</button-rounded-link>
    </div>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from "vue-property-decorator";
import ButtonRoundedLink from "@/components/Buttons/ButtonRoundedLink.vue";

interface INavLink {
  link: string;
  icon: string;
}

const dataListNavLinks: INavLink[] = [
  {
    link: "/",
    icon: "home",
  },
  {
    link: "/people",
    icon: "people",
  },
  {
    link: "/people",
    icon: "people",
  },
  {
    link: "/people",
    icon: "people",
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
  background-color: var(--color-bg-primary);
  border-radius: 25px;
  display: flex;
  flex-direction: column;
  align-items: center;
  &__item {
      margin-bottom: 2em;
  }
}
</style>
