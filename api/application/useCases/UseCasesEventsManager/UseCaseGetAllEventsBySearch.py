from api.application.ports.GetDataPort import GetDataBySearchPort

class UseCaseGetAllEventsBySearch():
    def __init__(self, getDataBySearchPort: GetDataBySearchPort):
        self.getDataBySearchPort = getDataBySearchPort
    
    def getAllFiltered(self, parameters):
        return self.getDataBySearchPort.getAllFiltered(parameters=parameters)