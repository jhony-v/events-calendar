from api.application.ports.UserManagemetPort import UpdateUserAccountPort
from api.domain.entities.User import User

class UserAccountUpdateRepository():
    def __init__(self, updateUserAccountPort: UpdateUserAccountPort):
        self.updateUserAccountPort = updateUserAccountPort

    def updateOutstandingAccount(self, userParameters):
        userModel = User(**userParameters)
        try:
            return self.updateUserAccountPort.updateOutstandingAccount(user=userModel)
        except Exception as e:
            pass
