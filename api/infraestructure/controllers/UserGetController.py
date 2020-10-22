from api.infraestructure.services.UserService.UserGet import UserGetService

def getUsers():
    userGetService = UserGetService()
    return userGetService.getUsers()

def getOneUserById(id):
    userGetService = UserGetService()
    return userGetService.getOneUserById(id)