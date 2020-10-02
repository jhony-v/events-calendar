<template>
  <card-flat class="card">
    <div class="card--col">
      <img :src="imageEvent" class="card__image-event" />
    </div>
    <div class="card--col">
      <div class="card__description-event">
        <div class="row-title">
          <text-label fontSizeText="medium" :weight="true">{{title}}</text-label>
        </div>
        <div class="row-user">
          <text-label variant="smooth" fontSizeText="regular">By</text-label>
          <text-label class="username" fontSizeText="regular">{{username}}</text-label>
        </div>
        <div class="row-date">
          <text-label variant="smooth" fontSizeText="small">
            <i class="date-icon material-icons">date_range</i>
          </text-label>
          <text-label variant="smooth" fontSizeText="small">{{datetime}}</text-label>
        </div>
      </div>
    </div>
  </card-flat>
</template>

<script lang="ts">
import { Vue, Component, Prop } from "vue-property-decorator";
import { CardFlat } from ".";
import { TextLabel } from "@/components/Common/TextLabels";

@Component({
  components: {
    CardFlat,
    TextLabel,
  },
})
export default class OutstandingCardEvent extends Vue {
  @Prop() imageEvent!: string;
  @Prop() title!: string;
  @Prop() username!: string;
  @Prop() datetime!: string;
}
</script>

<style lang="scss" scoped>
$card: card;
.#{$card} {
  background-color: rgba(0, 0, 0, 0.05);
  padding: 10px;
  display: flex;
  .#{$card}__image-event {
    height: 100%;
    width: 200px;
    border-radius: 10px;
  }
  .#{$card}__description-event {
    display: flex;
    margin-left: 15px;
    padding: 5px 0;
    flex-direction: column;
    height: 100%;
    .row-title {
      margin-bottom: 15px;
    }
    .row-user {
      .username {
        color: var(--color-primary);
        padding-left: 10px;
      }
    }
    .row-date {
      margin-top: auto;
      display: flex;
      align-items: center;
      .date-icon {
        margin-right: 10px;
      }
    }
  }
}
</style>
