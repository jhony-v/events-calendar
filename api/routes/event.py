from flask import Blueprint, jsonify, request
from utils import Response
import api.infraestructure.controllers.EventsGetController as eventGetController
import api.infraestructure.controllers.EventsCategoryGetController as eventsCategoryGetController
import json
eventRoute = Blueprint('event', __name__)

@eventRoute.route('/', methods=['GET'])
@eventRoute.route('/<int:eventId>', methods=['GET'])
def getAllEvents(eventId  = None):
    if eventId == None:
        start = request.args.get("start") if "start" in request.args else 0
        offset = request.args.get("offset") if "offset" in request.args else 4
        return Response(200,eventGetController.getAllEvents(start,offset))
    return Response(200,eventGetController.getEventById(eventId))

@eventRoute.route('/search', methods=['GET'])
def searchAllEvents():
    filters = dict(request.args)
    data = eventGetController.getAllEventsFiltered(filters=filters)
    return Response(200,data)

@eventRoute.route('/', method=['POST'])
def createNewEvent():
    return Response(200,{})

@eventRoute.route('/categories', methods=['GET'])
def getAllEventCategories():
    data = eventsCategoryGetController.getAllCategories()
    return Response(200,data)

@eventRoute.route('/<int:eventId>/comments', methods=['GET'])
def getAllCommentsByEvent(eventId):
    return Response(200,{})

@eventRoute.route('/', methods=['POST'])
def createNewEvent():
    request_json = request.get_json()
    eventImage = request.files['eventImage']
    return Response(200,{})


@eventRoute.route('/<int:eventId>', methods=['DELETE'])
def deleteEvent(idEvent):
    return Response(200,{})
