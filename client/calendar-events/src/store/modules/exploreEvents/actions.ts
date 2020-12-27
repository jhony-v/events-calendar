import { ActionTree } from "vuex";
import { ExploreEventsStore } from "./exploreEvents-types";
import ExploreEventsService from "@/infraestructure/services/ExploreEventsService";

const exploreEventsService = new ExploreEventsService();

const actions : ActionTree<ExploreEventsStore.ExploreEventsState,ExploreEventsStore.RootState> = {
}
export default actions;