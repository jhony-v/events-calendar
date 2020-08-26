<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<style lang="scss">
@import "./App";
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
  border-width: 0;
}

body {
  background: var(--color-bg-primary);
}
</style>
