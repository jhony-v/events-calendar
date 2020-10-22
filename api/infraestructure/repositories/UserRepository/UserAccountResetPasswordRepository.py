from api.domain.entities.User import User
from mysql.connector import MySQLConnection


class UserAccountResetPasswordRepository():
    def __init__(self, dataAccess: MySQLConnection):
        self.dataAccess = dataAccess

    def resetPassword(self, user: User):
        sql = "UPDATE User set password = %s WHERE email = %s"
        parametersPassword = (
            user.password,
            user.email,
        )   
        cursor = self.dataAccess.cursor();
        cursor.execute(sql,parametersPassword)
        cursor.close()
        return {}
