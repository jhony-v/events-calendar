from api.domain.entities.User import User

class UserValidatePropsSignIn():
    @staticmethod
    def issetProps(user: User):
        return user.password != "" and user.username != ""