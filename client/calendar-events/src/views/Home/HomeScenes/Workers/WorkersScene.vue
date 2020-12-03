<template>
  <div class="workers">
    <div class="workers__header">
      <div class="workers__main-title">
        <text-label :weight="true" fontSizeText="big"
          >Project workers</text-label
        >
      </div>
      <div class="workers__search">
        <input-field-search></input-field-search>
      </div>
    </div>
    <div class="workers__list">
      <div class="row--divider" v-for="(e,i) in data" :key="i">
        <row-project-worker :workerId="4" :full-name="'Fullname of user'"></row-project-worker>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { TextLabel } from "@/components/Common/TextLabels";
import InputFieldSearch from "@/components/Packages/FormControls/InputFieldSearch.vue";
import RowProjectWorker from "@/components/Packages/Workers/RowItems/RowProjectWorker.vue";
import { Vue, Component } from "vue-property-decorator";
@Component({
  components: {
    InputFieldSearch,
    RowProjectWorker,
    TextLabel,
  },
})
export default class WorkersScene extends Vue {
  private data = Array(10).fill(0);
}
</script>

<style lang="scss">

.workers {
  margin: 0 30px;

  &__main-title {
    flex: none;
    margin-right: 30px;
  }

  &__header {
    display: flex;
    align-items: center;
    margin: 2em auto 3em;
  }

  &__search {
    flex-grow: 1;
    display: flex;
  }

  &__list {
    .row--divider {
      border-bottom: 1px solid rgba(0,0,0,.1);
      padding: 1em 0;
    }
  }
}
</style>