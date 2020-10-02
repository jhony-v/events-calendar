from api.application.ports.UserManagemetPort import ResetPasswordPort
from api.infraestructure.adapters.adaptersDatabase.ExecuteDatabaseAdapter import ExecuteDatabaseAdapter
from api.domain.entities.User import User

class UserAccountResetPasswordRepository(ResetPasswordPort):
    def __init__(self, dataAccess: ExecuteDatabaseAdapter):
        self.dataAccess = dataAccess

    def resetPassword(self, oldPasswordUser: User, newPasswordUser: User):
        sql = "UPDATE User set password = %s WHERE password = %s AND id = %s"
        parametersPassword = (
            oldPasswordUser.password,
            newPasswordUser.password,
            newPasswordUser.id
        )
        executeResetPassword = self.dataAccess.execute(statement=sql, parameters=parametersPassword)
        return executeResetPassword
