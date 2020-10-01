from api.application.ports.AccessPort import SignInPort
from api.infraestructure.adapters.adaptersDatabase.ExecuteDatabaseAdapter import ExecuteDatabaseAdapter
from api.domain.entities.User import User

class SignInRepository(SignInPort):
    def __init__(self, dataAccess: ExecuteDatabaseAdapter):
        self.dataAccess = dataAccess

    def signIn(self, user: User):
        self.dataAccess.execute(statement="")
