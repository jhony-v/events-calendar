<template>
  <div class="item">
    <div class="item__col item__col--preview">
      <template v-if="isEditable">
        <input :value="defaultValue" :placeholder="title" />
      </template>
      <template v-else>
        <text-label>{{ title }}</text-label>
        <text-label>{{ defaultValue }}</text-label>
      </template>
    </div>
    <div class="item__col item__col--button-editable">
      <i class="material-icons" @click="onToggleEditValue">
        {{ computedGetIconEditable }}
      </i>
    </div>
  </div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from "vue-property-decorator";
import { TextLabel } from "@/components/Common/TextLabels";
@Component({
  components: {
    TextLabel,
  },
})
export default class OptionsListTabItemEditable extends Vue {
  private isEditable: boolean = false;

  @Prop() title!: string;
  @Prop() defaultValue!: string;

  onToggleEditValue() {
    this.isEditable = !this.isEditable;
  }

  get computedGetIconEditable() {
    return this.isEditable ? "close" : "dehaze";
  }
}
</script>

<style lang="scss" scoped>
.item {
  display: flex;
  padding: 15px 10px;
  align-items: center;
  justify-content: space-between;
  transition: 0.3s;
  border-bottom: 1px solid var(--color-text-neutral);

  &__col {
    &__button-editable {
      color: var(--color-text-neutral);
    }
  }
}
</style>
