from flask_sqlalchemy import SQLAlchemy
from flask import Flask

def database(app : Flask):
    db = SQLAlchemy(app)
    return db
