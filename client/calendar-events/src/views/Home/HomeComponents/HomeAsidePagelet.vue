<template>
  <div class="aside-pagelet">
    <card-flat>
      <div class="container">
        <navigator-aside></navigator-aside>
        <button-logout-link style="padding-bottom:1em" />
      </div>
    </card-flat>
  </div>
</template>

<script>
import { Vue, Component } from "vue-property-decorator";
import NavigatorAside from "@/components/Layouts/NavigatorAside/NavigatorAside.vue";
import { CardFlat } from "@/components/Common/Cards";
import { ButtonLogoutLink } from "@/components/Common/Buttons";

@Component({
  components: {
    NavigatorAside,
    CardFlat,
    ButtonLogoutLink,
  },
})
export default class HomeAsidePagelet extends Vue {}
</script>

<style lang="scss" scoped>
.aside-pagelet {
  width: 300px;
  padding: 1em 2em;
  flex: none;
  display: flex;
  align-items: stretch;
  > * {
    width: 100%;
  }
}
</style>
