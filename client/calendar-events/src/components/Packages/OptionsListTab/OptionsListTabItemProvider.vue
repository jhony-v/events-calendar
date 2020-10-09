<template>
  <div class="provider-tab">
    <div class="provider-tab-options">
        <slot name="provider-tab-options"></slot>
    </div>
    <div class="provider-tab-options-preview">
        <slot name="provider-tab-options-preview"></slot>
    </div>
  </div>
</template>

<script lang="ts">
import {  Vue,Component,ProvideReactive,Provide,Prop,Watch,Model,} from "vue-property-decorator";


export class OptionsListTabItemModel {
    constructor(
      public optionItemId : string = "", 
      public optionItemTitle : string = ""
    ){}
}

export interface IOptionsListTabItem{
  id : string;
  title : string;
}

@Component({})
export default class OptionsListTabItemProvider extends Vue {
  @Prop() initialItem!: IOptionsListTabItem;
  
  @Provide() optionItemModel : OptionsListTabItemModel = new OptionsListTabItemModel();
  @Provide() changeOptionItemId({id,title} : IOptionsListTabItem) {
    this.optionItemModel.optionItemId = id;
    this.optionItemModel.optionItemTitle = title;
  }

  created() {
    this.optionItemModel.optionItemId = this.initialItem.id;
    this.optionItemModel.optionItemTitle = this.initialItem.title;
  }
}
</script>

<style lang="scss" scoped>
.provider-tab {
    display: grid;
    grid-template-columns: 350px 1fr;
    &-options {
        border-right: 1px solid var(--color-border-neutral);
    }
}
</style>