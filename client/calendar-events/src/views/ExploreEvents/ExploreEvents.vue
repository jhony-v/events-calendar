<template>
  <div class="explore-events">
    
    <section-classification title-classification="Categories">
      <flat-list-scrollable-direction-controller :isHorizontal="true">
          <button-default 
            v-for="(value,key) in categoriesEvents" 
            :key="key"
            :style="{marginRight:'30px'}"
          >
            categorie
          </button-default>
      </flat-list-scrollable-direction-controller>
    </section-classification>

    <section-classification title-classification="Most relevants events">
      <flat-list-scrollable-direction-controller :isHorizontal="true">
        <article 
          v-for="(value,key) in mostRelevantEvents" 
          :key="key" 
          :style="{width:'500px',marginRight:'30px'}"
        >
          <outstanding-card-event 
          :title="value.title"
          :imageEvent="value.imageEvent"
          :datetime="value.datetime"
          :username="value.username">
          </outstanding-card-event>
        </article>
      </flat-list-scrollable-direction-controller>
    </section-classification>

    <section class="grid-events">
        <default-card-user-event
        v-for="(value,index) in allEvents"
        :key="index"
        :title="value.title"
        :image="value.imageEvent"
        :user="value.user"
        ></default-card-user-event>
    </section>

  </div>
</template>

<script lang="ts">
import SectionClassification from "@/components/Layouts/SectionClassification/SectionClassification.vue";
import { Component, Vue } from "vue-property-decorator";
import { OutstandingCardEvent, DefaultCardUserEvent } from "@/components/Common/Cards";
import { FlatListScrollableDirectionController } from '@/components/Common/Scrollables';
import { ButtonDefault } from '@/components/Common/Buttons';

@Component({
  components: {
    SectionClassification,
    ButtonDefault,
    OutstandingCardEvent,
    DefaultCardUserEvent,
    FlatListScrollableDirectionController
  },
})
export default class ExploreEvents extends Vue {
  mostRelevantEvents: any = Array(10)
    .fill({
      imageEvent: "https://cdn.pixabay.com/photo/2020/09/29/02/39/aircraft-5611528__340.jpg",
      title: "Desarrollo, evento de creación y desarrollo de sistemas información y animaciones controladas",
      datetime : "El día de mañana a las 6 am",
      username: "Larry Parker"
    } as any);
  categoriesEvents : any = Array(10)
    .fill({
    } as any);
  allEvents : any = Array(20).fill({
      imageEvent: "https://cdn.pixabay.com/photo/2016/11/06/17/17/north-america-1803504__340.jpg",
      title: "Desarrollo, evento de creación y desarrollo de",
      user: {
        avatar : "https://cdn.pixabay.com/photo/2020/09/23/02/01/microphone-5594702__340.jpg",
        email:"larry@hotmail.com",
        username: "Larry Parker"
      }
  } as any);
}
</script>

<style lang="scss" scoped>
.grid-events {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 40px;
  margin-top: 3em;
}
</style>
