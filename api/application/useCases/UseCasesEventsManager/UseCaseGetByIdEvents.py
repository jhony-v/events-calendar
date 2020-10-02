from api.application.ports.GetDataPort import GetDataById

class UseCaseGetByIdEvents():
    def __init__(self, getDataPort: GetDataById):
        self.getDataPort = getDataPort
        
    def getById(self, parameters):
        return self.getDataPort.getById(parameters=parameters)