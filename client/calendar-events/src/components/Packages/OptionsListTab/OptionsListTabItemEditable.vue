<template>
  <div class="item">
    <div class="item__col item__col--preview">
      <template v-if="isEditable">
        <input :value="defaultValue" :placeholder="title" class="item__input" />
      </template>
      <template v-else>
        <text-label fontSizeText="normal" class="title">{{ title }}</text-label>
        <text-label variant="smooth" fontSizeText="small">{{defaultValue}}</text-label>
      </template>
    </div>
    <div class="item__col item__button-editable">
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
    return this.isEditable ? "cancel" : "notes";
  }
}
</script>

<style lang="scss" scoped>
.item {
  display: flex;
  padding: 20px 10px;
  align-items: center;
  justify-content: space-between;
  transition: 0.3s background-color;
  border-bottom: 1px solid var(--color-border-neutral);

  &:hover {
      background-color:var(--color-primary-alpha-1);
  }

  &__col {
    &--preview {
      display: flex;
      flex-direction: column;
      width: 95%;
      .title {
        margin-bottom: 5px;
      }
    }
  }
  &__input {
    $p : 11px;
    padding-top: $p;
    padding-bottom: $p;
    background: none;
    cursor: pointer;
  }
  &__button-editable {
    color: var(--color-text-neutral);
    cursor: pointer;
  }
}
</style>
