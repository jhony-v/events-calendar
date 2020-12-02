<template>
  <div class="scene">
    <div class="scene__list">
      <flat-list-scrollable-direction-controller style="width:100%">
          <user-card-selectable 
          v-for="(value,index) in data" 
          :key="index"
          :title="value.title" 
          :detail="value.detail" 
          :image="value.image"
          :style="{marginBottom:'20px'}"></user-card-selectable>
      </flat-list-scrollable-direction-controller>
    </div>
    <div class="scene__preview">
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptatum quia sequi commodi unde quas officia perferendis? Assumenda quas dolorem quis deleniti officiis cupiditate earum explicabo. Rerum iure sit ad esse!
    </div>
  </div>
</template>

<script lang="ts">
import { UserCardSelectable } from '@/components/Common/Cards';
import { FlatListScrollableDirectionController } from '@/components/Common/Scrollables';
import { Vue, Component } from "vue-property-decorator";
@Component({
  components: {
    UserCardSelectable,
    FlatListScrollableDirectionController
  }
})
export default class HomeDefaultScenene extends Vue{ 
  data = Array(10).fill({
        image : "https://cdn.pixabay.com/photo/2020/09/23/02/01/microphone-5594702__340.jpg",
        title :"larry@hotmail.com",
        detail : "Larry Parker"
  })
};
</script>

<style lang="scss" scoped>
.scene {
  display: grid;
  grid-template-columns: 400px 1fr;
  &__preview {
    padding: 20px 5ex;
  }
}
</style>
