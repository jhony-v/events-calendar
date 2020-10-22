from api.infraestructure.repositories.DataAccessRepository import DataAccessRepository
from api.infraestructure.repositories.DataAccessRepository.MySQLRepository import MySQLRepository

class UserDeleteService(object):
    def __init__(self, client=DataAccessRepository(adapter=MySQLRepository)):
        self.client = client

    def deleteUserById(self, userId):
        sql = 'DELETE TABLE User WHERE userId = %s'
        return self.client.execute(sql, (userId,))
