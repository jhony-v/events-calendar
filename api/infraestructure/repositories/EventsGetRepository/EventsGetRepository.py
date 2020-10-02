from api.application.ports.GetDataPort import *
from api.infraestructure.adapters.adaptersDatabase.ExecuteDatabaseAdapter import ExecuteDatabaseAdapter

class EventsGetRepository(GetDataPort, GetDataBySearchPort, GetDataById):
    def __init__(self, dataAccess: ExecuteDatabaseAdapter):
        self.dataAccess = dataAccess

    def getAll(self, parameters):
        sql = "SELECT * FROM events LIMIT %s,%s"
        eventsRange = (
            parameters["start"],
            parameters["offset"]
        )
        return self.dataAccess.fetchAll(statement=sql, parameters=eventsRange)

    def getAllFiltered(self, parameters):
        sql = ""
        eventFilterParameters = ()
        return self.dataAccess.fetchAll(statement=sql,parameters=eventFilterParameters)

    def getById(self, idParameter: int):
        sql = "SELECT * FROM events WHERE id = %s"
        eventId = (idParameter)
        return self.dataAccess.fetch(statement=sql, parameters=eventId)
