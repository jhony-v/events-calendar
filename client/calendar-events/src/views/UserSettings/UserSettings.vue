<template>
  <div class="user-settings">
    <options-list-tab-item-provider :initial-item="{id:'a',title:'Account'}">
      <template #provider-tab-options>
        <settings-option-divider title="Personal">
          <options-list-tab-item tab-id="a" text="Account"></options-list-tab-item>
          <options-list-tab-item tab-id="b" text="General Profile"></options-list-tab-item>
          <options-list-tab-item tab-id="c" text="Contact"></options-list-tab-item>
        </settings-option-divider>
        <settings-option-divider title="Application">
          <options-list-tab-item tab-id="d" text="Theme app"></options-list-tab-item>
          <options-list-tab-item tab-id="e" text="Notifications"></options-list-tab-item>
        </settings-option-divider>
      </template>
      <template #provider-tab-options-preview>
        <options-list-tab-item-preview tab-id="a">
          <options-list-tab-item-editable title="Correo electronico" :defaultValue="'jhonyoaoha@gmail.com'"></options-list-tab-item-editable>
          <options-list-tab-item-editable title="Correo electronico" :defaultValue="'jhonyoaoha@gmail.com'"></options-list-tab-item-editable>
        </options-list-tab-item-preview>
        <options-list-tab-item-preview tab-id="b">
          <options-list-tab-item-editable title="Correo electronico" :defaultValue="'jhonyoaoha@gmail.com'"></options-list-tab-item-editable>
          <options-list-tab-item-editable title="Correo electronico" :defaultValue="'jhonyoaoha@gmail.com'"></options-list-tab-item-editable>
          <options-list-tab-item-editable title="Correo electronico" :defaultValue="'jhonyoaoha@gmail.com'"></options-list-tab-item-editable>
          <options-list-tab-item-editable title="Correo electronico" :defaultValue="'jhonyoaoha@gmail.com'"></options-list-tab-item-editable>
        </options-list-tab-item-preview>
        <options-list-tab-item-preview tab-id="c">
          <options-list-tab-item-editable title="Correo electronico" :defaultValue="'jhonyoaoha@gmail.com'"></options-list-tab-item-editable>
          <options-list-tab-item-editable title="Correo electronico" :defaultValue="'jhonyoaoha@gmail.com'"></options-list-tab-item-editable>
          <options-list-tab-item-editable title="Correo electronico" :defaultValue="'jhonyoaoha@gmail.com'"></options-list-tab-item-editable>
        </options-list-tab-item-preview>
      </template>
    </options-list-tab-item-provider>
  </div>
</template>

<script lang="ts">
import {
  OptionsListTabItem,
  OptionsListTabItemProvider,
  OptionsListTabItemEditable,
  OptionsListTabItemPreview,
} from "@/components/Packages/OptionsListTab";
import { Vue, Component } from "vue-property-decorator";
import SettingsOptionDivider from "./UserSettingsComponents/SettingsOptionDivider.vue";

@Component({
  components: {
    OptionsListTabItem,
    OptionsListTabItemProvider,
    OptionsListTabItemEditable,
    OptionsListTabItemPreview,
    SettingsOptionDivider,
  },
})
export default class UserSettings extends Vue {}
</script>

<style lang="scss" scoped>
.divider {
  padding-bottom: 3em;
}
</style>
