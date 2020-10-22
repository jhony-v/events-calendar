class DataAccessRepository(object):
    def __init__(self, adapter=None):
        self.client = adapter()
        self.fetchAll = lambda selector, params: self.client.fetchAll(selector, params)
        self.fetchOne = lambda selector, params: self.client.fetchOne(selector, params)
        self.execute = lambda selector, params: self.client.execute(selector, params)
        
