<template>
  <div class="button-iconify" @click="onClick">
      <i class="material-icons">{{computedCreateIconDynamic}}</i>
  </div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from "vue-property-decorator"

@Component({})
export default class ButtonRoundedIconify extends Vue {
  @Prop() icon !: string;
  @Prop() type !: string;
  
  onClick(e : HTMLDivElement) {
    this.$emit("click",e);
  }

  get computedCreateIconDynamic() {
    if(this.type) {
      const optionsTypeIcons : { [key : string] : string }  = {
        option : "more_vert",
        notification : "notifications",
        add: "add"
      }
      return optionsTypeIcons[this.type];
    }
    return this.icon
  }
}

</script>

<style lang="scss" scoped>
$size: 43px;
.button-iconify {
    flex: 0 0 auto;
    width: $size;
    height: $size;
    position: relative;
    border-radius: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: rgba(0,0,0,.05);
    color: var(--color-text-neutral-medium);
    filter: brightness(190%);
}
</style>