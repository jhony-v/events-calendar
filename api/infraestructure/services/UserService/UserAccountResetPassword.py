from api.domain.entities.User import User
from api.infraestructure.repositories.DataAccessRepository import DataAccessRepository
from api.infraestructure.repositories.DataAccessRepository.MySQLRepository import MySQLRepository

class UserAccountResetPasswordService(object):
    def __init__(self, client=DataAccessRepository(adapter=MySQLRepository)):
        self.client = client

    def resetPassword(self, user: User):
        sql = "UPDATE User set userPassword = %s WHERE email = %s"
        parametersPassword = (
            user.password,
            user.email,
        )
        return self.client.execute(sql, parametersPassword)
