<template>
  <card-flat class="card">
    <div class="card__header-event">
      <text-label :weight="true" fontSizeText="normal">{{ title }}</text-label>
      <img :src="image" class="card__image--primary" />
    </div>
    <div class="card__user">
      <user-card-selectable
        class="card__user--selectable"
        :detail="user.email"
        :image="user.avatar"
        :title="user.username"
      ></user-card-selectable>
    </div>
  </card-flat>
</template>

<script lang="ts">
import { Vue, Component, Prop } from "vue-property-decorator";
import { TextLabel } from "@/components/Common/TextLabels";
import { CardFlat, UserCardSelectable } from ".";

interface User {
  avatar?: string;
  username?: string;
  email?: string;
}

@Component({
  components: {
    TextLabel,
    CardFlat,
    UserCardSelectable,
  },
})
export default class DefaultCardUserEvent extends Vue {
  @Prop() title!: string;
  @Prop() image!: string;
  @Prop() user!: User;
}
</script>

<style lang="scss" scoped>
$card: card;
.#{$card} {
  padding: 30px 10px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.03);
  &__header-event {
    display: flex;
    flex-direction: column;
  }
  &__user {
    &--selectable {
      box-shadow: none;
    }
  }
  &__image {
    &--primary {
      border-radius: 10px;
      width: 100%;
      height: 150px;
      margin: 30px auto 20px;
      object-fit: cover;
    }
  }
}
</style>
