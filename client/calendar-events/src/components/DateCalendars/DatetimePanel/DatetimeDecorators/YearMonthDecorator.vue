<template>
  <div class="decorator">
    <span class="decorator__year">{{ computedGetYear }}</span>
    <span class="decorator__month">{{ computedGetMonth }}</span>
  </div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from "vue-property-decorator";
import moment from "moment";

@Component({})
export default class YearMonthDecorator extends Vue {
  @Prop() datetime!: string;

  get computedGetYear() {
    return moment(new Date(this.datetime)).year();
  }

  get computedGetMonth() {
    return moment(new Date(this.datetime)).month();
  }
}
</script>

<style lang="scss" scoped>
.decorator {
  display: flex;
  flex-direction: column;
  &__year {
    font-weight: 900;
    font-size: 3rem;
    color: var(--color-text-neutral-darker);
  }
  &__month {
    color: var(--color-text-neutral);
    font-size: 1.5rem;
    margin-top: 10px;
  }
}
</style>
