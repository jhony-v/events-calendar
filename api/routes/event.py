from flask import Blueprint, jsonify, request
import api.infraestructure.restControllers.EventsGetController as eventsController
eventRoute = Blueprint('event', __name__)

@eventRoute.route('/', methods=['GET'])
def getAllEvents():
    response = eventsController.getAllEvents( 
        start=request.args.get("start"),
        offset=request.args.get("offset")
    )
    return jsonify(response)


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
