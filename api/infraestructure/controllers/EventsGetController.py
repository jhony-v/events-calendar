from api.infraestructure.services.EventsService import EventsGetService

def getAllEvents(start: int, offset: int):
    getEventsService = EventsGetService()
    return getEventsService.getAll(parameters={
        "start": start,
        "offset": offset
    })

def getEventById(id: int):
    getEventsByIdService = EventsGetService()
    return getEventsByIdService.getById(parameters=id)
