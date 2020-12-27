import { API } from "../config/api";

export default class ExploreEventsService {
  getExploreCategories = async () => {
    try {
      const data: any = [
        {
          categoryId: 1,
          category: "Ventas",
        },
        {
          categoryId: 2,
          category: "Facturación",
        },
        {
          categoryId: 3,
          category: "Páginas web",
        },
        {
          categoryId: 4,
          category: "Inventarios",
        },
      ];
      return data;
    } catch (e) {
      throw new Error(e);
    }
  };

  getAllEventsToExplore = async () => {
    try {
      const data: any = {
        outstandings : [...Array(4)].map((e,i) => ({
            
        })),
        all : [...Array(10)].map((e,i) => ({
            
        })),
      };
      return data;
    } catch (e) {
      throw new Error(e);
    }
  };
}
