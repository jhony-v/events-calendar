<template>
    <div class="field-search">
        <input class="field-search__input" :ref="input" placeholder="Type a event to search..." />
        <button-rounded-iconify type="option"></button-rounded-iconify>
    </div>
</template>

<script lang="ts">
import { Vue, Component, Ref } from "vue-property-decorator";
import { ButtonRoundedIconify } from "@/components/Common/Buttons";

@Component({
    components: {
        ButtonRoundedIconify
    }
})
export default class InputFieldSearch extends Vue {
    @Ref() input !: HTMLInputElement;
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
    }
}
</style>