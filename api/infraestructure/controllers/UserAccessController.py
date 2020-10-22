from api.infraestructure.services.AuthService.UserSignIn import UserSignInService
from api.infraestructure.services.AuthService.UserSignUp import UserSignUpService
from api.infraestructure.helpers.JWTAuthenticate import JWTAuthenticate
from api.domain.entities.User import User

def signUpUser(user):
    signUpUserService = UserSignUpService()
    return signUpUserService.signUp(user=user)


def signInUser(user):
    userModel = User()
    userModel.email = user['email']
    userModel.password = user['password']
    signInUserService = UserSignInService()
    data = signInUserService.signIn(user=userModel)
    if data : 
        return {
            'token' : JWTAuthenticate().encode(data)
        }
    else:
        return {}