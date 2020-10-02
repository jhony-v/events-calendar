<template>
  <div class="navigate">
      <button-rounded-iconify type="add"></button-rounded-iconify>
      <button-rounded-iconify type="notification"></button-rounded-iconify>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from "vue-property-decorator";
import { ButtonRoundedIconify } from "@/components/Common/Buttons";

@Component({
    components:{
        ButtonRoundedIconify
    }
})
export default class OptionsNavigate extends Vue{

}
</script>

<style lang="scss" scoped>
.navigate {
    display: flex;
}   
</style>