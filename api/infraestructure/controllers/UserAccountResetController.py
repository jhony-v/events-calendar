from api.infraestructure.repositories.UserRepository.UserAccountResetPasswordRepository import UserAccountResetPasswordRepository
from databases import mysqlConnection
from api.domain.entities.User import User
from api.infraestructure.helpers.EncryptPassword import EncryptPassword

def resetPassword(email,password):
    user = User()
    user.email = email
    user.password = EncryptPassword.encrypt(password)

    resetPasswordRepository = UserAccountResetPasswordRepository(dataAccess=mysqlConnection)
    return resetPasswordRepository.resetPassword(user)
