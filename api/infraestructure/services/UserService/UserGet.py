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
        sql = 'SELECT userId,username,userDescription,profileImage,fullName,email,backgroundImage FROM user WHERE userId = %s'
        return self.client.fetchOne(sql, (userId,))

    def getEventsByUserId(self, userId):
        sql = "select * from `Event` where createdByUserId = %s"
        return self.client.fetchAll(sql, (userId,))
    
    def getEventsAndCreatorByUserId(self,userId):
        user = self.getOneUserById(userId)
        events = self.getEventsByUserId(userId)
        return {
            'user': {
                **user,
                'events': events
            },
        }