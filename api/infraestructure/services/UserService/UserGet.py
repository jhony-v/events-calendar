from api.domain.entities.User import User
from api.infraestructure.repositories.DataAccessRepository import DataAccessRepository
from api.infraestructure.repositories.DataAccessRepository.MySQLRepository import MySQLRepository

class UserGetService(object):
    def __init__(self, client=DataAccessRepository(adapter=MySQLRepository)):
        self.client = client

    def getUsers(self):
        sql = 'SELECT * FROM User'
        return self.client.fetchAll(sql)

    def getOneUserById(self, userId):
        sql = 'SELECT * FROM user WHERE userId = %s'
        return self.client.fetchOne(sql, (userId,))
