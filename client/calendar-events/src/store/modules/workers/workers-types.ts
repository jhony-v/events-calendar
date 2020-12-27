export namespace WorkersStore {
  export interface RootState {}
  export interface Worker {
    userId: number;
    avatar: string;
    fullName: string;
    totalJobs: number;
    jobs: any[];
  }
  export interface WorkersState {
    loading: boolean;
    failed: boolean;
    workers: Worker[];
  }
  export enum WorkerActions {
    FETCH_WORKERS = "FETCH_WORKERS",
    LOADING = "LOADING",
  }
}
