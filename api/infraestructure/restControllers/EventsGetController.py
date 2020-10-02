from api.infraestructure.repositories.EventsGetRepository.EventsGetRepository import *
from api.infraestructure.dataAccess.MySQL import MySQL
from api.application.useCases.UseCasesEventsManager.UseCaseGetAllEvents import UseCaseGetAllEvents
from api.application.useCases.UseCasesEventsManager.UseCaseGetByIdEvents import UseCaseGetByIdEvents

def getAllEvents(start: int, offset: int):
    getEventsRepository = EventsGetRepository(dataAccess=MySQL)
    useCasesGetEvents = UseCaseGetAllEvents(getDataPort=getEventsRepository)
    return useCasesGetEvents.getAll(parameters={
        "start": start,
        "offset": offset
    })

def getEventById(id: int):
    getEventByIdRepository = EventsGetRepository(dataAccess=MySQL)
    useCaseGetAllEvents = UseCaseGetByIdEvents(getDataPort=getEventByIdRepository)
    return useCaseGetAllEvents.getById(parameters=id)
