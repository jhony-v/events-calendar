from api.application.ports.GetDataPort import GetDataPort, GetDataBySearchPort
from api.infraestructure.adapters.adaptersDatabase.ExecuteDatabaseAdapter import ExecuteDatabaseAdapter

class EventsGetRepository(GetDataPort, GetDataBySearchPort):
    def __init__(self, dataAccess: ExecuteDatabaseAdapter):
        self.dataAccess = dataAccess

    def getAll(self):
        return self.dataAccess.execute(statement="")

    def getAllFiltered(self, parameters):
        return self.dataAccess.execute(statement="")
