from api.infraestructure.repositories.EventsGetRepository.EventsGetRepository import EventsGetRepository
from databases import mysqlConnection

def getAllEvents(start: int, offset: int):
    getEventsRepository = EventsGetRepository(dataAccess=mysqlConnection)
    return getEventsRepository.getAll(parameters={
        "start": start,
        "offset": offset
    })

def getEventById(id: int):
    getEventsByIdRepository = EventsGetRepository(dataAccess=mysqlConnection)
    return getEventsByIdRepository.getById(parameters=id)
