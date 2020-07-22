from flask import Flask
from flask_cors import CORS
from utils import REGISTER_PATHS
from api import api as apiRouters

class Server:
    def initialize(self):
        app = Flask(__name__)
        CORS(app)
        REGISTER_PATHS(app,apiRouters,'/api/v1/')
        return app
