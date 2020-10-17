from mysql.connector import MySQLConnection
from api.domain.entities.User import User
import json
class UserGetRepository():
    def __init__(self, dataAccess: MySQLConnection):
        self.dataAccess = dataAccess

    def getUsers(self):
        sql = 'SELECT * FROM user'
        data = {}
        cursor = self.dataAccess.cursor(dictionary=True)
        cursor.execute(sql)
        data = cursor.fetchall()
        return data

    def getOneUserById(self, userId):
        sql = 'SELECT * FROM user WHERE userId = %s'
        data = {}
        cursor = self.dataAccess.cursor(dictionary=True)
        cursor.execute(sql, (userId,))
        data = cursor.fetchone()
        cursor.close()
        return data
