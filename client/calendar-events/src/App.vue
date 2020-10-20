<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>
<script lang="ts">
import { Vue, Component } from "vue-property-decorator";
import { Action } from 'vuex-class';

@Component({})
export default class App extends Vue {
  @Action("authCheckUser",{namespace:"auth"}) authCheckUser !: () => void;
  created() {
    this.authCheckUser();
  }
}
</script>
<style lang="scss">
@import "./App";
</style>
