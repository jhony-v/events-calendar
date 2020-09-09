<template>
  <div class="aside-pagelet">
    <navigator-aside></navigator-aside>
  </div>
</template>

<script>
import { Vue, Component } from "vue-property-decorator";
import NavigatorAside from "@/components/Layouts/NavigatorAside/NavigatorAside.vue";

@Component({
  components: {
    NavigatorAside,
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
