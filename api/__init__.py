from api.routes import user,event
from flask import Flask

def apiRoutes(app : Flask):
    app.register_blueprint(user.userRoute,url_prefix='/api/v1/users')    
    app.register_blueprint(event.eventRoute,url_prefix='/api/v1/events')