from api.application.ports.AccessPort import SignUpPort
from api.domain.entities.User import User

class SignUpRepository(SignUpPort):
    def __init__(self, dataAccess: ExecuteDatabaseAdapter):
        self.dataAccess = dataAccess

    def signUp(self, user: User):
        sql = "INSERT INTO User(username,email,password) VALUES (%s,%s,%s)"
        userParams = (
            user.username,
            user.email,
            user.password
        )
        executeUserSignUp = self.dataAccess.execute(statement=sql,parameters=userParams)
        return executeUserSignUp