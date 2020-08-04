
Vue.component("card-datetime", {
  props : [ "datetime", "description" ],
  template: `
    <div class="card-datetime">
        <div class="card-datetime__date">
            <div class="date__day--number">{{getDate}}</div>
            <div class="date__day--text">
                <div class="month">Sunday</div>
                <div class="year">{{'september'}}, {{getFullYear}}</div>
            </div>
          </div>
        <div class="card-datetime__subject">
            <div class="description">{{description}}</div>
            <div class="time">Program at {{getTime}}</div>
        </div>
    </div>
    `,
    computed : {
        getFullYear(){
            return new Date(this.datetime).getFullYear();
        },
        getDate() {
            return new Date(this.datetime).getDate();
        },
        getTime() {
            return new Date(this.datetime).toLocaleTimeString();
        }
    },
    created() {
        console.log(new Date(this.datetime))
    }
});
