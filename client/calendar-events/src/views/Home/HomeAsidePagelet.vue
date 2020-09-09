<template>
  <div class="aside-pagelet">
    <card-flat>
      <div class="container">
        <navigator-aside></navigator-aside>
        <button-logout-link style="padding-bottom:1em">Salir</button-logout-link>
      </div>
    </card-flat>
  </div>
</template>

<script>
import { Vue, Component } from "vue-property-decorator";
import NavigatorAside from "@/components/Layouts/NavigatorAside/NavigatorAside.vue";
import CardFlat from '@/components/Cards/CardFlat.vue';
import ButtonLogoutLink from '@/components/Buttons/ButtonLogoutLink.vue';

@Component({
  components: {
    NavigatorAside,
    CardFlat,
    ButtonLogoutLink
  },
})
export default class HomeAsidePagelet extends Vue {}
</script>

<style lang="scss" scoped>
.aside-pagelet {
    width: 300px;
    padding: 1em 2em 0;
    flex: none;
}
</style>
