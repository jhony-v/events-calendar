<template>
  <div class="item" @click="onClick">
    <div class="item__col">
        <text-label fontSizeText="normal">{{text}}</text-label>
    </div>
    <div class="item__col">
        <i class="material-icons">chevron_right</i>
    </div>
  </div>
</template>

<script lang="ts">
import { TextLabel } from '@/components/Common/TextLabels';
import { Vue , Component, Prop } from "vue-property-decorator";

@Component({
    components : {
        TextLabel,
    }
})
export default class OptionsListTabItem extends Vue{
    @Prop() text !: string;
    onClick() {
        this.$emit("click");
    }
}
</script>

<style lang="scss" scoped>

.item {
    display: flex;
    padding:15px 10px;
    align-items: center;
    justify-content: space-between;
    transition: .3s;
    border-bottom: 1px solid var(--color-text-neutral);
}

</style>