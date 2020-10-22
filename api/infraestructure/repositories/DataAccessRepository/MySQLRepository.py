from databases import mysqlConnection
from mysql.connector import MySQLConnection

class MySQLRepository(object):
    def __init__(self):
        self.db: MySQLConnection = mysqlConnection

    def executeCursor(self, selector: str, params: tuple, multi: bool = False):
        cursor = self.db.cursor(dictionary=True)
        cursor.execute(selector, params, multi)
        return cursor

    def executeCommit(self):
        self.db.commit()

    def fetchAll(self, selector, params: tuple = None):
        cursor = self.executeCursor(selector, params)
        data = cursor.fetchall()
        cursor.close()
        return data

    def fetchOne(self, selector, params: tuple = None):
        cursor = self.executeCursor(selector, params)
        data = cursor.fetchone()
        cursor.close()
        return data

    def execute(self, selector, params: tuple = None):
        cursor = self.executeCursor(selector, params)
        self.executeCommit()
        return {}
