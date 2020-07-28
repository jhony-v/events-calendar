from client import main
from flask import Flask

def clientRoutes(app : Flask):
        app.register_blueprint(main.mainRoute,url_prefix='')