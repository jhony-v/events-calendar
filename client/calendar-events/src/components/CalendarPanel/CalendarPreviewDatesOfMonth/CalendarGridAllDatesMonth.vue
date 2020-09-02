<template>
    <div class="grid-all-dates">
        <calendar-item-grid-date v-for="(value,key) in dates" :key="key"> 
            {{key}}
        </calendar-item-grid-date>
    </div>
</template>

<script lang="ts">
import { Vue, Component } from "vue-property-decorator";
import CalendarItemGridDate from "./CalendarItemGridDate.vue";

@Component({
    components : {
        CalendarItemGridDate
    }
})
export default class CalendarGridAllDaysMonth extends Vue {
    private dates : number[] = Array(35).fill(0);
}
</script>

<style lang="scss" scoped>
.grid-all-dates {
    display: grid;
    grid-template-columns: repeat(7,1fr);
}
</style>