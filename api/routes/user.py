from flask import Blueprint, jsonify

userRoute = Blueprint('user', __name__)

@userRoute.route('/', methods = ['GET'] )
def getAllUsers():
    return jsonify([])

@userRoute.route('/', methods = ['POST'] )
def createNewUser():
    return jsonify([])

@userRoute.route('/<int:idUser>', methods = ['DELETE'] )
def deleteUser( idUser ):
    return jsonify([])
