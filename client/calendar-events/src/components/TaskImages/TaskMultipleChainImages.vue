<template>
  <div class="task-multiple">
    <div class="image__collection">
      <avatar-image v-for="(image, index) in images" :key="index" :src="image" class="image__item"></avatar-image>
    </div>
  </div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from "vue-property-decorator";
import AvatarImage from "../Interface/AvatarImage.vue";

@Component({
  components: {
    AvatarImage,
  }
})
export default class TaskMultipleChainImages extends Vue {
  @Prop() images!: string[];
}
</script>

<style lang="scss" scoped>
.task-multiple {
  .image__collection {
    display: inline-block;
    position: relative;
    .image__item {
      position: relative;
      @for $i from 0 through 3 {
        &:nth-child(#{$i}) {
          margin-left: $i * -0.2em;
        }
      }
    }
  }
}
</style>
