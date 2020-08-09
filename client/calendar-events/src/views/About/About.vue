<template>
  <div class="about">
    <h1>This is an about page {{duplicate}}</h1>
  </div>
</template>
<script lang="ts">
import {Component, Vue} from 'vue-property-decorator';

@Component({})
export default class About extends Vue {
  get duplicate() {
    return Number(this.$route.params.id) * 2;
  }
}

</script>