<template>
  <div class="error-404">
    <div class="error-404__container">
      <div class="error-404__header">
        <div class="error-404__title">404</div>
        <div class="error-404__title--message">Page not found</div>
      </div>
      <div class="error-404__body">
        <div class="error-404__message">
            Sorry, we cant find the page you are looking for click 
            <router-link to="/" class="redirect">Here</router-link> 
            to come back to home page
        </div>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import { Vue } from "vue-property-decorator";
export default class Error404 extends Vue {}
</script>
<style lang="scss">
.error-404 {
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  &__container {
     margin: auto;  
  }   
  &__header {
    text-align: center;
  }
  &__title {
    font-size: 5em;
    color: var(--color-primary-dark);
    text-shadow: 0 10px 20px rgba(0,0,0,.25);
    &--message {
        color: var(--color-primary-dark-medium);
        font-weight: bold;
        font-size: 1.8em;
    }
  }
  &__message {
      text-align: center;
      padding:2em;
      margin: auto;
      width: 500px;
      color: var(--color-primary-dark);
      font-size: .9rem;
      line-height: 22px;
      margin-top: 1em;
}
}

.redirect {
    color: var(--color-primary);        
    font-weight: bold;  
    text-shadow: 0 0 30px currentColor;
}
</style>
