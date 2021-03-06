from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from datetime import datetime
from time import time

db = SQLAlchemy()

class Luggage(db.Model):
    __tablename__ = 'luggage'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    ticket = db.Column(db.String(11))
    location = db.Column(db.String(11))
    bagCount = db.Column(db.Integer)
    loggedIn = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User',
                             backref=db.backref('luggage', lazy='joined'))
    
    def __init__(self, name, ticket, location, bagCount, user):
        self.name = name
        self.ticket = ticket
        self.location = location
        self.bagCount = bagCount
        self.user = user
    
    def __repr__(self):
        pass
    
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(30), unique=True)
    pin = db.Column(db.String(10), unique=True)
    
    def __init__(self, userName, pin):
        self.userName = userName
        self.pin = pin
        
    def __repr__(self):
        pass

        
#engine = create_engine('sqlite:///./Luggage.db')
#db.metadata.create_all(bind=engine)        
