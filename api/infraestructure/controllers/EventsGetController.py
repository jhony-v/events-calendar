from api.infraestructure.services.EventsService.EventsGet import EventsGetService

def getAllEvents(start: int, offset: int):
    getEventsService = EventsGetService()
    return getEventsService.getAllEvents(limits={
        "start": int(start),
        "offset": int(offset)
    })


def getEventById(id: int):
    getEventsByIdService = EventsGetService()
    return getEventsByIdService.getEventById(eventId=id)


def getAllEventsFiltered( filters : dict ):
    return EventsGetService().getAllEventsFiltered(filters=filters)