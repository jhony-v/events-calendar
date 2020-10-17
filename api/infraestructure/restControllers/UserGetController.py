from api.infraestructure.repositories.UserGetRepository.UserGetRepository import UserGetRepository
from databases import mysqlConnection


def getUsers():
    userGetRepository = UserGetRepository(dataAccess=mysqlConnection)
    return userGetRepository.getUsers()

def getOneUserById(id):
    userGetRepository = UserGetRepository(dataAccess=mysqlConnection)
    return userGetRepository.getOneUserById(id)