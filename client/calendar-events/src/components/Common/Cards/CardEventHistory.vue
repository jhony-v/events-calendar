<template>
  <card-flat class="card-event">
    <div class="card-event__image">
      <img :src="eventImage" class="image-event" />
    </div>
    <div class="card-event__detail-user">
        <avatar-image :src="user.avatar" :sizeImage="35" class="image-user"></avatar-image>
        <text-label :weight="true" fontSizeText="small">{{user.username}}</text-label>
    </div>
  </card-flat>
</template>

<script lang="ts">
import { Vue, Component, Prop } from "vue-property-decorator";
import { CardFlat } from ".";
import { AvatarImage } from "@/components/Common/AvatarImages"
import { TextLabel } from "@/components/Common/TextLabels"

interface User {
    avatar ?: string;
    username ?: string; 
}

@Component({
  components: {
    CardFlat,
    AvatarImage,
    TextLabel
  },
})
export default class CardEventHistory extends Vue {
    @Prop() eventImage !: string;
    @Prop() user !: User;
}
</script>

<style lang="scss" scoped>
.card-event {
  padding: 10px;
  width: 180px;
  &__image {
    .image-event {
        border-radius: 15px;
        width: 100%;
        height: 250px;
        -webkit-user-drag: none;
    }
  }
  &__detail-user {
    display: flex;
    align-items: center;
    margin-top: 15px;
    .image-user {
        margin-right: 5px;
    }
  }
}
</style>
