from api.infraestructure.repositories.UserAccountManagerRepository.UserDeleteRepository import UserDeleteRepository
from databases import mysqlConnection


def deleteUserById(userId):
    userRepository = UserDeleteRepository(dataAccess=mysqlConnection)
    return userRepository.deleteUserById(userId)
