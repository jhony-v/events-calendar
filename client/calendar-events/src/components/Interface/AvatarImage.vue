<template>
  <div class="avatar">
    <svg :width="sizeImage" :height="sizeImage" class="avatar--svg" :data-variant="variant">
      <image :href="src" x="0" y="0" width="100%" height="100%" preserveAspectRatio="xMidYMid slice" class="image"></image>
    </svg>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
type variantAvatar = "yes" | "no";

@Component({})
export default class AvatarImage extends Vue {
  @Prop() src !: string;
  @Prop({default:50}) sizeImage !: number;
  @Prop({default:"no"}) variant !: variantAvatar;
}
</script>

<style lang="scss">
.avatar {
  display: inline-block;
  &--svg {
    border-radius: 100%;
    margin: auto;
    &[data-variant="yes"] {
      border: 2px solid var(--color-primary);
      padding: 4px;
    }
  }
}
</style>
