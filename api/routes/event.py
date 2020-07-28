from flask import Blueprint, jsonify

eventRoute = Blueprint('event', __name__)

@eventRoute.route('/<int:idEvent>', methods=['GET'])
def getAllEventsById(idEvent):
    return jsonify([])


@eventRoute.route('/<int:idEvent>/users', methods=['GET'])
def getAllUsersByEvent(idEvent):
    return jsonify([])


@eventRoute.route('/<int:idEvent>/comments', methods=['GET'])
def getAllCommentsByEvent(idEvent):
    return jsonify([])


@eventRoute.route('/', methods=['POST'])
def createNewEvent():
    return jsonify([])


@eventRoute.route('/<int:idEvent>', methods=['DELETE'])
def deleteEvent(idEvent):
    return jsonify([])
