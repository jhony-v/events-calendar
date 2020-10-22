class DataAccessRepository(object):
    def __init__(self, adapter=None):
        self.client = adapter()
        self.fetchAll = lambda selector, params = None: self.client.fetchAll(selector, params)
        self.fetchOne = lambda selector, params = None: self.client.fetchOne(selector, params)
        self.execute = lambda selector, params = None: self.client.execute(selector, params)
        
