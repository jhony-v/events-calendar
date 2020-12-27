<template>
  <div class="worker worker--row">
    <div class="worker__user-detail">
      <avatar-image
        :src="avatar"
        variant="featured"
      ></avatar-image>
      <router-link :to="workerId">
        <text-label :weight="true" class="link--hover-underline">{{fullName}}</text-label>
      </router-link> 
    </div>
    <div class="worker__total-jobs">
      <text-label :weight="true" class="total">{{totalJobs}}</text-label>
      <text-label variant="smooth">Projectos trabajando</text-label>
    </div>
    <div class="worker__options">
      <button-default>{{textActionButton}}</button-default>
    </div>
  </div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from "vue-property-decorator";
import { AvatarImage } from "@/components/Common/AvatarImages";
import { ButtonDefault } from "@/components/Common/Buttons";
import { TextLabel } from "@/components/Common/TextLabels";

@Component({
  components: {
    TextLabel,
    AvatarImage,
    ButtonDefault,
  },
})
export default class RowProjectWorker extends Vue {
  @Prop() workerId !: number;
  @Prop() avatar !: string;
  @Prop() fullName !: string;
  @Prop() totalJobs !: string;
  @Prop({default:'JOBS'}) textActionButton !: string;
}
</script>

<style lang="scss">

.worker {
  &.worker--row {
    display: flex;
    align-items: center;
  }
  &__user-detail {
    display: flex;
    align-items: center;
    > :last-child {
      margin-left: 10px;
    }
    .link--hover-underline:hover{
      text-decoration: underline;
    }
  }
  &__total-jobs {
    margin-left: auto;
    margin-right:20px;
    .total {
      margin-right: 10px;
    }
  }
  &__options {
    .button {
      margin-left: 10px;
    }
  }
}
</style>