from api.infraestructure.repositories.DataAccessRepository import DataAccessRepository
from api.infraestructure.repositories.DataAccessRepository.MySQLRepository import MySQLRepository

class EventsGetService(object):
    def __init__(self, client=DataAccessRepository(adapter=MySQLRepository)):
        self.client = client

    def getAllEvents(self, limits):
        sql = "SELECT * FROM Event LIMIT %s,%s"
        eventsRange = (
            limits["start"],
            limits["offset"],
        )
        return self.client.fetchAll(sql, eventsRange)

    def getAllEventsFiltered(self, parameters):
        sql = ""
        eventFilterParameters = ()
        pass
        # return self.dataAccess.fetchAll(statement=sql,parameters=eventFilterParameters)

    def getEventById(self, eventId: int):
        sql = "SELECT * FROM Event WHERE id = %s"
        return self.client.fetchOne(sql, (eventId,))

    def getEventByUserId(self, parameterId: int):
        sql = "select * from `Event` where createdByUserId = %s"
        return self.client.fetchAll(sql, (parameterId,))
