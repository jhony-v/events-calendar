from run import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    fullName = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(500), nullable=False)
    profileImage = db.Column(db.String(500), nullable=True)
