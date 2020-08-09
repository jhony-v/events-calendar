<template>
  <div id="app">
    <theme-provider :theme="theme">
      <router-view />
    </theme-provider>
  </div>
</template>

<style lang="scss">
* {
  box-sizing: border-box;
  font-family: Arial, Helvetica, sans-serif;
  margin: 0;
  padding: 0;
}

a {
  text-decoration: none;
}

button,
textarea,
summary,
details,
input {
  outline: none;
}
</style>
<script lang="ts">
import Vue from "vue";
import { ThemeProvider } from "vue-styled-components";
import light from "./themes/light";
export default Vue.extend({
  data: () => ({
    theme: light,
  }),
  components: {
    "theme-provider": ThemeProvider,
  },
});
</script>
