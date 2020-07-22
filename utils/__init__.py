from flask import Flask

def REGISTER_PATHS(app: Flask,routers,prefix):
    for current in routers :
        app.register_blueprint(current['router'],url_prefix=prefix+current['path'])
