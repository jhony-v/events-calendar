import { ActionTree } from "vuex";
import { WorkersStore } from "./workers-types";
import WorkersService from "@/infraestructure/services/WorkersService";


const workersService = new WorkersService();

const actions : ActionTree<WorkersStore.WorkersState,WorkersStore.RootState> = {
    async fetchWorkers({commit}) {
        commit(WorkersStore.WorkerActions.LOADING);
        const data = await workersService.fetchWorkers();
        commit(WorkersStore.WorkerActions.FETCH_WORKERS,data);
    }
}
export default actions;