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

    def getAllEventsFiltered(self, filters : dict):
        filterValues = {}
        query = "SELECT * FROM Event WHERE "
        i = 1
        for key, value in filters.items():
            query += f"{key} LIKE %({key})s"
            filterValues[key] = "%{}%".format(value)
            if i < len(filters):
                query += ' AND '
            i += 1
        return self.client.fetchAll(query,filterValues)

    def getEventById(self, eventId: int):
        sql = "SELECT * FROM Event WHERE eventId = %s"
        return self.client.fetchOne(sql, (eventId,))
