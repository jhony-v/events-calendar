<template>
  <div class="new-event">
    <div class="new-event__header">
      <text-label :weight="true" fontSizeText="big"
        >Create new event</text-label
      >
    </div>
    <div class="new-event__body">
      <div class="new-event__form">
        <div class="form__controls"></div>
        <div class="form__date-picker">
          <calendar-panel-container> </calendar-panel-container>
        </div>
        <div class="form__options">
          <button-default>CANCELAR</button-default>  
          <button-app-primary>CREATE NEW EVENT</button-app-primary>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { ButtonAppPrimary, ButtonDefault } from "@/components/Common/Buttons";
import { TextLabel } from "@/components/Common/TextLabels";
import CalendarPanelContainer from "@/components/Packages/DateCalendars/CalendarPanel/CalendarPanel.vue";
import { Vue, Component } from "vue-property-decorator";
@Component({
  components: {
    CalendarPanelContainer,
    TextLabel,
    ButtonAppPrimary,
    ButtonDefault,
  },
})
export default class NewEventScene extends Vue {}
</script>

<style lang="scss">
$form: form;
.new-event {
  margin: 0 30px;
  &__#{$form} {
    display: flex;
    margin-top: 40px;
    flex-wrap: wrap;
  }
  .#{$form} {
    &__controls {
      flex: none;
      width: 360px;
      padding-right: 90px;
    }
    &__date-picker {
      flex-grow: 1;
      background: red;
    }
    &__options {
      width: 100%;
      display: flex;
      margin: 40px 0 0;
      justify-content: flex-end;
      > * {
          margin-left: 20px;
      }
    }
  }
}
</style>