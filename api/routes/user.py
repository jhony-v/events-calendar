from flask import Blueprint, request, make_response
from api.repositories.UserAuthRepository import UserAuthRepository
from api.repositories.UserActionsBasicRepository import UserActionsBasicRepository
from utils import Response

userRoute = Blueprint('user', __name__)

@userRoute.route('/', methods=['GET'])
def getAllUsers():
    users = UserActionsBasicRepository.getAllUsers()
    return Response(True, {
        'users': users
    })

@userRoute.route('/', methods=['POST'])
def createNewUser():
    deleteUser = UserActionsBasicRepository.createUser()
    return Response(True, '')

@userRoute.route('/<int:idUser>', methods=['DELETE'])
def deleteUser(idUser):
    user = UserActionsBasicRepository.deleteUser(idUser)
    if user:
        return Response(True, {
            'id': user
        })

@userRoute.route('sign-in', methods=['POST'])
def signInUser():
    request_json = request.get_json()
    if request_json['username'] and request_json['password']:
        userRepository = UserAuthRepository.authenticate(request_json['username'], request_json['password'])
        if userRepository:
            return Response(True, {
                'jwt': userRepository
            })
        else:
            return Response(False, '')
