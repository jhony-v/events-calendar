<template>
  <div class="main-drawer-pagelet">
    <card-flat>
      <div class="container">
        <tabs-browser-panel :data-links="data" alignment="right"></tabs-browser-panel>
        <calendar-panel></calendar-panel>
      </div>
    </card-flat>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from "vue-property-decorator";
import CalendarPanel from "@/components/CalendarPanel/CalendarPanel.vue";
import TabsBrowserPanel, { DataLinkTabBrowser } from '@/components/Layouts/TabsBrowserPanel/TabsBrowserPanel.vue';
import CardFlat from '@/components/Cards/CardFlat.vue';

@Component({
  components: {
    CalendarPanel,
    TabsBrowserPanel,
    CardFlat
  },
})
export default class MainDrawerPagelet extends Vue {
  private data !: DataLinkTabBrowser[];
  created(){
    this.data = [
      {
      to : "/",
      text : "item 1"
    },
          {
      to : "/s",
      text : "item 2"
    },
    {
      to : "/s",
      text : "item 3"
    },
    {
      to : "/s",
      text : "item 4"
    }
    ];
  }
}
</script>

<style lang="scss" scoped>
.main-drawer-pagelet {
    width: 100%;
    padding: 1em 2em 0;
    .container {
      padding: 1em;
    }
}
</style>
