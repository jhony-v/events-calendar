from run import db
from api.models.User import User

class UserActionsBasicRepository:

    @staticmethod
    def deleteUser(userId):
        try:
            user = User.query.filter_by(id=userId)
            db.session.delete(user)
            db.session.commit()
            return True
        except Exception as error:
            return False

    @staticmethod
    def createUser():
        try:
            user = User()
            db.session.add(user)
            db.session.commit()
            return True if user else False
        except Exception as error :
            return False
    
    @staticmethod
    def getAllUsers():
        user = User.query.all();
        return user