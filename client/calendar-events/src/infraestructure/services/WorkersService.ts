import { API } from "../config/api";
import faker from "faker";

export default class WorkersService {
  async fetchWorkers() {
    try {
      // const request = await API.get("/workers");
      // return request.data;
      return [...Array(20)].map((item, index) => {
        return {
          userId: index,
          avatar : faker.random.image(),
          fullName: faker.name.firstName(),
          totalJobs: Math.floor(Math.random() * 10),
          jobs: [],
        };
      });
    } catch (e) {
      throw new Error(e);
    }
  }
}
