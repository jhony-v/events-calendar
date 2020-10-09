<template>
    <div class="preview">
        <text-label v-if="computedIsActiveItem" :weight="true" class="title">{{title}}</text-label>
        <slot v-if="computedIsActiveItem"></slot>
    </div>
</template>
<script lang="ts">
import { TextLabel } from '@/components/Common/TextLabels';
import { Vue, Component, Inject, Prop } from "vue-property-decorator";
import { OptionsListTabItemModel } from "./OptionsListTabItemProvider.vue";

@Component({
  components: {
    TextLabel
  }
})
export default class OptionsListTabItemPreview extends Vue {
  @Prop() tabId!: string;
  @Inject() optionItemModel!: OptionsListTabItemModel;

  get title() {
    return this.optionItemModel.optionItemTitle;
  }

  get computedIsActiveItem() {
    return this.tabId === this.optionItemModel.optionItemId;
  }
}
</script>

<style lang="scss" scoped>
.title {
  display: block;
  padding-left: 10px;
  padding-bottom: 20px;
}
</style>