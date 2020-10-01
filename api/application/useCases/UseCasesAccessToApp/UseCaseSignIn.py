from api.application.ports.AccessPort import SignInPort
from api.domain.entities.User import User
from api.application.validations.UserValidatePropsSignIn import *

class UseCaseSignIn():
    def __init__(self,signInPort: SignInPort):
        self.signInPort = signInPort
    def signIn(self, userParameters ):
        user = User(**userParameters)
        if UserValidatePropsSignIn.issetProps(user):
            return self.signInPort.signIn(user)