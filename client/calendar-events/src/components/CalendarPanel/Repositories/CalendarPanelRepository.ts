import moment from "moment";

export interface CalendarCurrentDate {
  date: moment.Moment;
  isInCurrentMonth: boolean;
}

export default class CalendarPanelRepository {
  getAllDatesByMonth = (dateMonth: moment.Moment): CalendarCurrentDate[] => {
    let dates: CalendarCurrentDate[] = [];
    let firstDate = moment(dateMonth).startOf("month");
    let lastDate = moment(dateMonth).endOf("month");

    while (firstDate.day() !== 1) firstDate.subtract(1, "day");
    while (lastDate.day() !== 0) lastDate.add(1, "day");
    
    while (firstDate.isSameOrBefore(lastDate)) {
      dates.push({
        date: moment(firstDate),
        isInCurrentMonth: firstDate.month() === dateMonth.month(),
      });
      firstDate.add(1, "day");
    }
    
    return dates;
  };
}
