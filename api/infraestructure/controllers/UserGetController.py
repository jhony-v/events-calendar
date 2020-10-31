from api.infraestructure.services.UserService.UserGet import UserGetService

def getUsers():
    return UserGetService().getUsers()

def getOneUserById(userId):
    return UserGetService().getOneUserById(userId)

def getEventsByUserId(userId):
    return UserGetService().getEventsAndCreatorByUserId(userId)
