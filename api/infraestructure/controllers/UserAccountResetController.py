from api.domain.entities.User import User
from api.infraestructure.helpers.EncryptPassword import EncryptPassword
from api.infraestructure.services.UserService.UserAccountResetPassword import UserAccountResetPasswordService

def resetPassword(email,password):
    user = User()
    user.email = email
    user.password = EncryptPassword.encrypt(password)
    resetPasswordService = UserAccountResetPasswordService()
    return resetPasswordService.resetPassword(user)
