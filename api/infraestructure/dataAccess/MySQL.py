import api.infraestructure.adapters.adaptersDatabase.CreateDatabaseAdapter as Create
import api.infraestructure.adapters.adaptersDatabase.FetchDatabaseAdapter as Fetch
import api.infraestructure.adapters.adaptersDatabase.DeleteDatabaseAdapter as Delete


class MySQL(Fetch.GetAllDatabaseAdapter, Create.CreateNewDataDatabaseAdapter, Delete.DeleteDatabaseAdapter):
    def __init__(self):
        pass

    def getAll(self, statement):
        try:
            return statement
        except Exception as e:
            return e
    