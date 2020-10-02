from api.application.ports.AccessPort import SignInPort
from api.domain.entities.User import User
from api.infraestructure.adapters.adaptersDatabase.ExecuteDatabaseAdapter import ExecuteDatabaseAdapter

class SignInRepository(SignInPort):
    def __init__(self, dataAccess: ExecuteDatabaseAdapter):
        self.dataAccess = dataAccess

    def signIn(self, user: User):
        sql = "SELECT * FROM user WHERE email = %s AND password = %s"
        userParams = (
            user.email,
            user.password
        )
        fetchUserSignIn = self.dataAccess.fetch(statement=sql,parameters=userParams)
        return fetchUserSignIn if fetchUserSignIn else {}