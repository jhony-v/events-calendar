from api.infraestructure.repositories.DataAccessRepository import DataAccessRepository
from api.infraestructure.repositories.DataAccessRepository.MySQLRepository import MySQLRepository

class EventsCreateService(object):
    def __init__(self, client=DataAccessRepository(adapter=MySQLRepository)):
        self.client = client

    def createNewEvent(self):
        sql = 'INSERT INTO Event(title,description,eventImage,startDate,endDate,eventCategoryId,createdByUserId) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)';
        paramEvents = ()
        data = self.client.execute(sql,paramEvents)
        return data