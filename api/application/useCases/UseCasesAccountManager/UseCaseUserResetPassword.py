from api.application.ports.UserManagemetPort import ResetPasswordPort
from api.domain.entities.User import User

class UseCaseUserResetPassword():
    def __init__(self, resetPasswordPort: ResetPasswordPort):
        self.resetPasswordPort = resetPasswordPort

    def resetPassword(self,userId : int, oldPassword: str, newPassword: str):
        oldUser = User()
        newUser = User()
        oldUser.password = oldPassword
        newUser.password = newPassword
        newPassword.id = userId
        return self.resetPasswordPort.resetPassword(oldPasswordUser=oldUser,newPasswordUser=newUser)
