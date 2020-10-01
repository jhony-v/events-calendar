from api.domain.entities.User import User

class UpdateUserAccountPort(object):
    def updateOutstandingAccount(self, user : User):
        pass
    
class ResetPasswordPort(object):
    def resetPassword(self, oldPassword: str, newPassword: str):
        pass
