import { Module } from "vuex";
import actions from './actions'
import mutations from './mutations'
import { WorkersStore } from "./accountSettings-types";

const workers : Module<WorkersStore.WorkersState,WorkersStore.RootState> = {
    namespaced : true,
    state : {
        failed : false,
        loading : true,
        workers : []
    },
    mutations,
    actions,
}

export default workers;