<template>
  <div class="profile">
    <flex-wrapper alignment="right">
      <button-rounded-iconify type="option"></button-rounded-iconify>
    </flex-wrapper>
    <flex-wrapper class="profile__user">

      <!-- user avatar image profile -->
      <avatar-image class="profile__avatar" :sizeImage="200" src="https://cdn.pixabay.com/photo/2020/10/06/11/50/puppy-5632005__340.jpg"></avatar-image>
      
      <!-- user global detail information -->
      <div class="profile__detail">
        <div class="profile__user--username">
            <text-label :weight="true" :block="true" fontSizeText="big">Jhony vega cuya</text-label>
            <text-label variant="smooth" fontSizeText="small" :block="true">jhonyvega@gmail.com</text-label>
        </div>
        <div class="profile__user--totals">
            <flex-wrapper>
            <div class="profile__user-point" v-for="i in [1,2,4]" :key="i">
                    <flex-wrapper>
                        <text-label :weight="true" style="margin-right:8px">253</text-label>
                        <text-label variant="smooth" style="margin-right:50px"> publications</text-label>
                    </flex-wrapper>
                </div>
            </flex-wrapper>
        </div>
        <div class="profile__user--description">
            <text-label variant="smooth" fontSizeText="normal">
                Elon Reeve Musk FRS is a business magnate, industrial designer, engineer, and philanthropist. 
                He is the founder, CEO, CTO and chief designer of SpaceX; 
                early investor, CEO and product architect of Tesla, Inc.; founder of The Boring Company; co-founder of
            </text-label>
        </div>
      </div>
    
    </flex-wrapper>
    <flex-wrapper class="profile__tabs"> 
        
    </flex-wrapper>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from "vue-property-decorator";
import { AvatarImage } from "@/components/Common/AvatarImages";
import { ButtonRoundedIconify } from "@/components/Common/Buttons";
import { FlexWrapper } from "@/components/Common/Wrappers";
import { TextLabel } from "@/components/Common/TextLabels";

@Component({
  components: {
    FlexWrapper,
    TextLabel,
    AvatarImage,
    ButtonRoundedIconify,
  },
})
export default class Profile extends Vue {}
</script>

<style lang="scss" scoped>
.profile {
    &__detail {
        margin-left: 25px;
    }
    &__user {
        &--totals {
            margin-top: 25px;
            margin-bottom: 2em;
        }
        &--description {
            margin-top: 3em;
        }
    }
}
</style>
