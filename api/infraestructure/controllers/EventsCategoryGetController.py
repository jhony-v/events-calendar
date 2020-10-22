from api.infraestructure.services.EventsService.EventCategoryGet import EventCategoryGetService

def getAllCategories(): 
    return EventCategoryGetService().getAllCategories()