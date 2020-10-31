from api.infraestructure.services.UserService.UserDelete import UserDeleteService

def deleteUserById(userId):
    userDeleteService = UserDeleteService()
    return userDeleteService.deleteUserById(userId)
