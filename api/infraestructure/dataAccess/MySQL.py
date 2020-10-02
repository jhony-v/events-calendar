import api.infraestructure.adapters.adaptersDatabase.ExecuteDatabaseAdapter as DatabaseAdapter
from databases import mysqlConnection

class MySQL(DatabaseAdapter.ExecuteDatabaseAdapter):
    def __init__(self):
        self.connection = mysqlConnection

    def cmd(self):
        try:
            return self.connection.cursor()
        except Exception as e:
            return e

    def fetchAll(self, statement: str, parameters: tuple):
        with self.connection() as cursor:
            cursor.execute(statement, parameters)
            return cursor.fetchAll()

    def fetch(self, statement: str, parameters: tuple):
        with self.cmd() as cursor:
            cursor.execute(statement, parameters)
            return cursor.fetchOne()

    def execute(self, statement: str, parameters: tuple):
        with self.cmd() as cursor:
            cursor.execute(statement, parameters)
        self.connection.commit()

    def __delete__(self):
        self.connection.close()
