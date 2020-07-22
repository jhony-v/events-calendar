from flask import Flask
from flask_cors import CORS
from utils import REGISTER_PATHS
from api import routers

class Server:
    def initialize(self):
        app = Flask(__name__)
        CORS(app)
        REGISTER_PATHS(app,routers,'/api/v1/')
        return app
