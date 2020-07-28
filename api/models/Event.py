from run import db
from datetime import datetime

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100),nullable=False)
    description = db.Column(db.String(300), nullable=False)
    create = db.Column(db.DateTime,default=datetime.utcnow)