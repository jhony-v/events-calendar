from flask import Flask
from flask_cors import CORS
from config import UPLOAD_FOLDER 

def serverApp():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    CORS(app)
    return app
