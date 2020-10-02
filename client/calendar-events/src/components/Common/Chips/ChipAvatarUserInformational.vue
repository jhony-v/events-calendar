<template>
  <div class="chip-user-informational">
    <div class="avatar">
      <avatar-image :src="image"></avatar-image>
    </div>
    <div class="user" @click="onClickUser">
      <text-label :weight="true">{{ username }}</text-label>
      <text-label fontSizeText="small" variant="smooth">{{ detail }}</text-label>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import {AvatarImage} from "@/components/Common/AvatarImages";
import {TextLabel} from "@/components/Common/TextLabels";

@Component({
  components: {
    AvatarImage,
    TextLabel,
  },
})
export default class ChipAvatarUserInformational extends Vue {
  @Prop() image!: string;
  @Prop() username!: string;
  @Prop() detail!: string;
  onClickUser() {
      this.$emit("click");
  }
}
</script>

<style lang="scss" scoped>
.chip-user-informational {
  display: flex;
  align-items: center;
  .avatar {
      margin-right: 10px;
  }
  .user {
      cursor: pointer;
      display: flex;
      flex-direction: column;
  }
}
</style>
