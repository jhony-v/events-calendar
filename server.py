from flask import Flask
from flask_cors import CORS

def serverApp():
    app = Flask(__name__)
    CORS(app)
    return app
