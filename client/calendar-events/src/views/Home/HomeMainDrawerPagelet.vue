<template>
  <div class="main-drawer-pagelet">
    <card-flat>
      <div class="container">
        <router-view></router-view>
      </div>
    </card-flat>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from "vue-property-decorator";
import CardFlat from '@/components/Cards/CardFlat.vue';

@Component({
  components: {
    CardFlat
  },
})
export default class MainDrawerPagelet extends Vue {
}
</script>

<style lang="scss" scoped>
.main-drawer-pagelet {
    width: 100%;
    padding: 1em 2em 0;
    .container {
      padding: 1em;
    }
}
</style>
