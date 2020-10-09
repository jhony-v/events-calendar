<template>
<div :class="computedClassOptionItem" @click="onClick">
    <div class="item__col">
      <text-label fontSizeText="normal">{{ text }}</text-label>
    </div>
    <div class="item__col">
      <i class="material-icons text">chevron_right</i>
    </div>
  </div>
</div>
</template>

<script lang="ts">
import { TextLabel } from "@/components/Common/TextLabels";
import { Vue, Component, Prop, InjectReactive, Inject, Model } from "vue-property-decorator";
import { OptionsListTabItemModel, IOptionsListTabItem } from './OptionsListTabItemProvider.vue';

@Component({
  components: {
    TextLabel,
  },
})
export default class OptionsListTabItem extends Vue {
  @Prop() text!: string;
  @Prop() tabId!: string;
  @Inject() optionItemModel !: OptionsListTabItemModel;
  @Inject() changeOptionItemId !: (valueOptionItemId: IOptionsListTabItem) => void;
 
  get computedIsActiveItem() {
    return this.tabId === this.optionItemModel.optionItemId;
  }

  get computedClassOptionItem() {
    return ["tab__col","item", { active: this.computedIsActiveItem }];
  }

  onClick() {
    this.changeOptionItemId({
      id : this.tabId,
      title : this.text
    });
  }
}
</script>

<style lang="scss" scoped>
.item {
  display: flex;
  padding: 20px 10px;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid var(--color-border-neutral);
  border-right: 3px solid transparent;
  transition: .3s;
  cursor: pointer;
  &:last-of-type {
    border-bottom: none; 
  }
  &.active {
      border-right-color: var(--color-primary);
      background-color:var(--color-primary-alpha-1);
  }
}
</style>
