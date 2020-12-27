<template>
    <div class="field-search">
        <input class="field-search__input" :ref="input" :placeholder="searchPlaceholder" />
        <button-rounded-iconify type="option"></button-rounded-iconify>
    </div>
</template>

<script lang="ts">
import { Vue, Component, Ref, Prop } from "vue-property-decorator";
import { ButtonRoundedIconify } from "@/components/Common/Buttons";

@Component({
    components: {
        ButtonRoundedIconify
    }
})
export default class InputFieldSearch extends Vue {
    @Ref() input !: HTMLInputElement;
    @Prop({default:"Ingresar texto a buscar..."}) searchPlaceholder !: string;
}
</script>

<style lang="scss" scoped>
.field-search {
    display: flex;
    width: 100%;
    &__input {
        margin-right: 1em;
        padding: 10px;
        border-radius: 20px;
        width: 100%;
        background-color: rgba(0,0,0,.05);
    }
}
</style>