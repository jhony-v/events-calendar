from os import environ,path
from dotenv import load_dotenv

baseDir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(baseDir,'../.env'))

SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = False