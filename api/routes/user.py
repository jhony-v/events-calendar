from flask import Blueprint, request, make_response, jsonify
from utils import Response
import api.infraestructure.controllers.UserAccessController as accessController
import api.infraestructure.controllers.UserGetController as userGetController
from api.infraestructure.helpers.EncryptPassword import EncryptPassword
import api.infraestructure.controllers.UserDeleteController as userDeleteController
import api.infraestructure.controllers.UserAccountResetController as userResetController

userRoute = Blueprint('user', __name__)

@userRoute.route('/', methods=['GET'])
@userRoute.route('/<int:userId>', methods=['GET'])
def getAllUsers(userId = 0):
    data = userGetController.getUsers() if userId == 0 else userGetController.getOneUserById(userId)
    return Response(200,data);


@userRoute.route('/reset-password', methods = ['POST'])
def resetUserPassword():
    request_json = request.get_json()
    data = userResetController.resetPassword(email=request_json['email'],password=request_json['password'])
    return Response(200,data)


@userRoute.route('/<int:userId>', methods=['DELETE'])
def deleteUser(userId):
    data = userDeleteController.deleteUserById(userId)
    return Response(201,data)


@userRoute.route('sign-in', methods=['POST'])
def signInUser():
    request_json = request.get_json()
    data = accessController.signInUser(user={
       'email' : request_json['email'],
       'password' : request_json['password']     
    })
    return Response(200,data)
    
@userRoute.route('sign-up', methods=['POST'])
def signUpUser():
    request_json = request.get_json()
    username = 'username'
    password = 'password'
    email = 'email'
    if username in request_json and password in request_json:
        userSignUpController = accessController.signUpUser(user={
            'username': request_json[username],
            'password': EncryptPassword.encrypt(request_json[password]),
            'email': request_json[email]
        })
        return Response(200, userSignUpController)