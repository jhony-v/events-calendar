from api.domain.entities.User import User
from mysql.connector import MySQLConnection

class SignUpRepository():
    def __init__(self,dataAccess : MySQLConnection):
        self.dataAccess = dataAccess

    def signUp(self, user: User):
        sql = "INSERT INTO `User`(username,email,userPassword) VALUES (%s,%s,%s)"
        userParams = (
            user['username'],
            user['email'],
            user['password']
        )
        with self.dataAccess.cursor() as cursor:
            cursor.execute(sql, userParams)
        self.dataAccess.commit()
        self.dataAccess.close()
        return {}
