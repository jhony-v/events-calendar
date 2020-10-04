<template>
  <div class="classification">
    <div class="classification--header">
        <text-label fontSizeText="regular" :weight="true">{{titleClassification}}</text-label>
        <text-label fontSizeText="normal" :weight="true" class="classification__button">Ver más</text-label>
    </div>
    <div class="classification--body">
        <slot></slot>
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
export default class SectionClassification extends Vue {
    @Prop() titleClassification !: string;
}
</script>

<style lang="scss" scoped>
.classification {
    padding: 20px 0 40px;
    &--header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding-bottom: 20px;
    }
    &__button {
        color: var(--color-primary);
    }
}
</style>
