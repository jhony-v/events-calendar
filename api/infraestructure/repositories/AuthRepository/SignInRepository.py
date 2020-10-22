from api.domain.entities.User import User
from mysql.connector import MySQLConnection
from api.infraestructure.helpers.EncryptPassword import EncryptPassword


class SignInRepository():
    def __init__(self, dataAccess: MySQLConnection):
        self.dataAccess = dataAccess

    def fetch(self, query, params: tuple):
        cursor = self.dataAccess.cursor(dictionary=True)
        cursor.execute(query, params)
        data = cursor.fetchone()
        return data

    def signIn(self, user: User):
        sql = "SELECT email,userPassword FROM user WHERE email = %s"
        userParams = (user.email,)
        data = self.fetch(sql, userParams)
        if data != None and EncryptPassword.validate(user.password, data['userPassword']):
            sql = "SELECT email,userId FROM user WHERE email = %s"
            return self.fetch(sql, userParams)
        else:
            return {}
