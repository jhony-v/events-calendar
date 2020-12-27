export namespace ExploreEventsStore {
  export interface RootState {}

  export interface Categories {
    categoryId: number;
    category: string;
  }
  export interface Event {
    eventId: number;
    title: string;
    createdDate: string;
    finishedDate: string;
    image: string;
    creator: {
      userId: number;
      fullName: string;
      avatar: string;
      email: string;
    };
  }

  export interface ExploreEventsState {
    categories: Categories[];
    outstandingsEvents: Event[];
    allEvents: Event[];
    loading: boolean;
  }
  export enum ExploreActions {
    FETCH_EVENTS = "FETCH_EVENTS",
    LOADING = "LOADING",
  }
}
