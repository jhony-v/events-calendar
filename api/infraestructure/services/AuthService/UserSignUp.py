from api.domain.entities.User import User
from api.infraestructure.repositories.DataAccessRepository import DataAccessRepository
from api.infraestructure.repositories.DataAccessRepository.MySQLRepository import MySQLRepository

class UserSignUpService(object):
    def __init__(self, client=DataAccessRepository(adapter=MySQLRepository)):
        self.client = client

    def signUp(self, user: User):
        sql = 'INSERT INTO `User`(username,email,userPassword) VALUES (%s,%s,%s)'
        userParams = (
            user['username'],
            user['email'],
            user['password'],
        )
        data = self.client.execute(sql, userParams)
        return data
