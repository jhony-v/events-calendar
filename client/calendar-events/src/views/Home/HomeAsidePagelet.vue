<template>
  <div class="aside-pagelet">
    <card-flat>
      <div class="container">
        <navigator-aside></navigator-aside>
      </div>
    </card-flat>
  </div>
</template>

<script>
import { Vue, Component } from "vue-property-decorator";
import NavigatorAside from "@/components/Layouts/NavigatorAside/NavigatorAside.vue";
import CardFlat from '@/components/Cards/CardFlat.vue';

@Component({
  components: {
    NavigatorAside,
    CardFlat
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
