<template>
  <card-flat>
    <div class="card--event">
      <text-label>{{ title }}</text-label>
      <img :src="image" />
    </div>
    <div class="card--user">
      <user-card-selectable
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

<style lang="scss" scoped></style>
