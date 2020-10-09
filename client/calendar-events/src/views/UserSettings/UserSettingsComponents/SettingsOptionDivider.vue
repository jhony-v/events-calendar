<template>
  <div class="divider">
      <text-label :weight="true" class="divider__title">{{title}}</text-label>
      <slot></slot>
  </div>
</template>

<script lang="ts">
import { TextLabel } from '@/components/Common/TextLabels';
import { Vue, Component, Prop } from "vue-property-decorator";
@Component({
    components:{
        TextLabel        
    }
})
export default class UserSettings extends Vue {
    @Prop() title !: string;
}
</script>

<style lang="scss" scoped>
.divider {
    padding-bottom: 3em;
    &__title {
        display: block;
        padding-left: 10px;
        margin-bottom: 20px;
    }
}
</style>