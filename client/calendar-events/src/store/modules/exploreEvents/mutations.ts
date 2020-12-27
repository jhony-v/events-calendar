import { MutationTree } from "vuex";
import { WorkersStore } from "./exploreEvents-types";

const mutations  : MutationTree<WorkersStore.WorkersState> = {
    [WorkersStore.WorkerActions.LOADING] : (state) => {
        state.loading = true;
    },
    [WorkersStore.WorkerActions.FETCH_WORKERS] : (state,workers : any)  => {
        state.workers = workers;
    }
}
export default mutations;