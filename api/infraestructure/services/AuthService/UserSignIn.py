from api.domain.entities.User import User
from api.infraestructure.helpers.EncryptPassword import EncryptPassword
from api.infraestructure.repositories.DataAccessRepository import DataAccessRepository
from api.infraestructure.repositories.DataAccessRepository.MySQLRepository import MySQLRepository

class UserSignInService(object):
    def __init__(self, client = DataAccessRepository(adapter=MySQLRepository)):
        self.client = client

    def signIn(self, user: User):
        userParams = (user.email,)
        data = self.client.fetchOne('SELECT email,userPassword FROM user WHERE email = %s',userParams)
        if data != None and EncryptPassword.validate(user.password, data['userPassword']):
            return self.client.fetchOne('SELECT email,userId FROM user WHERE email = %s',userParams)
        else:
            return {}