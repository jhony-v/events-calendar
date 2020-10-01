from flask import Blueprint, request, make_response
from utils import Response

userRoute = Blueprint('user', __name__)

@userRoute.route('/', methods=['GET'])
def getAllUsers():
    pass

@userRoute.route('/', methods=['POST'])
def createNewUser():
    pass

@userRoute.route('/<int:idUser>', methods=['DELETE'])
def deleteUser(idUser):
    pass

@userRoute.route('sign-in', methods=['POST'])
def signInUser():
    request_json = request.get_json()
    if request_json['username'] and request_json['password']:
        pass
