from api.infraestructure.repositories.DataAccessRepository import DataAccessRepository
from api.infraestructure.repositories.DataAccessRepository.MySQLRepository import MySQLRepository

class EventCategoryGetService(object):
    def __init__(self, client=DataAccessRepository(adapter=MySQLRepository)):
        self.client = client

    def getAllCategories(self):
        sql = 'SELECT * FROM EventCategory'
        return self.client.fetchAll(sql)