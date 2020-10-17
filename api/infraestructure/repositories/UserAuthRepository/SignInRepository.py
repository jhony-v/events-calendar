from api.domain.entities.User import User
from mysql.connector import MySQLConnection
from api.infraestructure.transforms.EncryptPassword import EncryptPassword

class SignInRepository():
    def __init__(self, dataAccess: MySQLConnection):
        self.dataAccess = dataAccess

    def signIn(self, user: User):
        sql = "SELECT * FROM user WHERE email = %s"
        email = user['email']
        password = user['password']

        userParams = (email)

        with self.dataAccess.cursor() as cursor:
            cursor.execute(sql,userParams)
            data = cursor.fetchone()
            if(EncryptPassword.validate(password,data['password'])):
                return data
            else:
                return {}
        self.dataAccess.close()
