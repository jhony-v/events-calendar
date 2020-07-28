from run import db
from datetime import datetime

class UserEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dateCreated = db.Column(db.String, nullable=False, default=datetime.utcnow)
    dateFinished = db.Column(db.DateTime,nullable=False)
    idUser = db.Column(db.Integer, db.ForeignKey('user.id'))
    idEvent = db.Column(db.Integer, db.ForeignKey('event.id'))
