from api.infraestructure.repositories.UserRepository.UserDeleteRepository import UserDeleteRepository
from databases import mysqlConnection


def deleteUserById(userId):
    userRepository = UserDeleteRepository(dataAccess=mysqlConnection)
    return userRepository.deleteUserById(userId)
