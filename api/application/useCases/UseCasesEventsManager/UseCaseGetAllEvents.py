from api.application.ports.GetDataPort import GetDataPort

class UseCaseGetAllEvents():
    def __init__(self, getDataPort: GetDataPort):
        self.getDataPort = getDataPort
    def getAll(self, parameters: dict):
        return self.getDataPort.getAll(parameters=parameters)