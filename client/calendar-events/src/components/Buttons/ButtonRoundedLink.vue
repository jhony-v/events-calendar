<template>
  <router-link
    :to="to"
    class="link-button"
    active-class="link-button--selected"
  >
    <div class="icon">
      <i class="material-icons">
        <slot></slot>
      </i>
    </div>
    <span class="text">{{ text }}</span>
  </router-link>
</template>

<script lang="ts">
import { Vue, Component, Prop } from "vue-property-decorator";

@Component({})
export default class ButtonRoundedLink extends Vue {
  @Prop() to!: string;
  @Prop() text!: string;
  @Prop() icon!: string;
}
</script>
<style lang="scss" scoped>
.link-button {
  text-align: center;
  display: block;
  .icon {
    $size: 60px;
    margin: auto;
    width: $size;
    height: $size;
    border-radius: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--color-text-neutral);
    flex: none;
  }
  .text {
    font-weight: bold;
    color: var(--color-text-neutral);
    display: inline-block;
    margin-top: 10px;
    font-size: .8rem;
  }
  &--selected {
    .icon {
      background-color: var(--color-primary);
      color: white;
      box-shadow: 0 15px 30px 10px var(--color-border-neutral);
    }
    .text {
      color: var(--color-text-neutral-darker);
    }
  }
  &:not(&--selected) {
    .icon {
      border: 1px solid var(--color-text-neutral);
    }
  }
}
</style>
