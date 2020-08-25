from run import db
from api.models.User import User
import jwt
from config import JWT_KEY


class UserAuthRepository():
    @staticmethod
    def authenticate(username: str, password: str):
        try :
            user = User.query.filter_by(
                username=username, password=password).first()
            if user:
                jwtEncode = jwt.encode(user, JWT_KEY)
                return jwtEncode
            return False
        except Exception as error : 
            return False