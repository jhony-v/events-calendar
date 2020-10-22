from api.infraestructure.repositories.AuthRepository.SignUpRepository import SignUpRepository
from api.infraestructure.repositories.AuthRepository.SignInRepository import SignInRepository
from databases import mysqlConnection
from api.domain.entities.User import User
from api.infraestructure.helpers.JWTAuthenticate import JWTAuthenticate

def signUpUser(user):
    signUpUserRepository = SignUpRepository(dataAccess=mysqlConnection)
    return signUpUserRepository.signUp(user=user)


def signInUser(user):
    userModel = User()
    userModel.email = user['email']
    userModel.password = user['password']
    signInUserRepository = SignInRepository(dataAccess=mysqlConnection)
    data = signInUserRepository.signIn(user=userModel)
    if data : 
        return {
            'token' : JWTAuthenticate().encode(data)
        }
    else:
        return {}