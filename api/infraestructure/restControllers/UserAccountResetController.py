from api.infraestructure.repositories.UserAccountManagerRepository.UserAccountResetPassword import UserAccountResetPasswordRepository
from databases import mysqlConnection
from api.domain.entities.User import User
from api.infraestructure.transforms.EncryptPassword import EncryptPassword

def resetPassword(email,password):
    user = User()
    user.email = email
    user.password = EncryptPassword.encrypt(password)

    resetPasswordRepository = UserAccountResetPasswordRepository(dataAccess=mysqlConnection)
    return resetPasswordRepository.resetPassword(user)
