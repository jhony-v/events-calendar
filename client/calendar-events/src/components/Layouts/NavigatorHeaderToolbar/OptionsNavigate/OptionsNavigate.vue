<template>
  <div class="navigate">
    <input-field-search></input-field-search>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from "vue-property-decorator";
import InputFieldSearch from "@/components/Packages/FormControls/InputFieldSearch.vue";

@Component({
    components:{
        InputFieldSearch
    }
})
export default class OptionsNavigate extends Vue{

}
</script>

<style lang="scss" scoped>
.navigate {
    width: 500px;
    margin: auto;
}   
</style>