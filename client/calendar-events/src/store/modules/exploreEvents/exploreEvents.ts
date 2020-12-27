import { Module } from "vuex";
import actions from './actions'
import { ExploreEventsStore } from "./exploreEvents-types";
import mutations from './mutations'

const workers : Module<ExploreEventsStore.ExploreEventsState,ExploreEventsStore.RootState> = {
    namespaced : true,
    state : {
        allEvents : [],
        categories : [],
        outstandingsEvents : [],
        loading : true,
    },
    mutations,
    actions,
}

export default workers;