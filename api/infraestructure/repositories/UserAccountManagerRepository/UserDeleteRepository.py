from mysql.connector import MySQLConnection


class UserDeleteRepository():
    def __init__(self, dataAccess: MySQLConnection):
        self.dataAccess = dataAccess

    def deleteUserById(self, userId):
        sql = 'DELETE TABLE User WHERE userId = %s'
        cursor = self.dataAccess.cursor()
        cursor.execute(sql, (userId,))
        self.dataAccess.commit()
        cursor.close()
        return {}
