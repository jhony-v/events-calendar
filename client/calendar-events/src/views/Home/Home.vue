<template>
  <div class="home">
    <loading-spinner label="Verificando datos"></loading-spinner>
  </div>
</template>

<script lang="ts">

import { Vue, Component } from "vue-property-decorator";
import LoadingSpinner from '@/components/styled/LoadingSpinner.vue';

@Component({
  components : {
    LoadingSpinner
  }
})
export default class Home extends Vue {

}
</script>
