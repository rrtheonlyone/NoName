from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
from flask_sqlalchemy import *
import ast

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_API'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
api = Api(app)

class Person(db.Model):
    personId = db.Column(db.Integer, primary_key=True)
    personName = db.Column(db.String(120), nullable=False)
    # foods = db.relationship('Food', secondary=foods, lazy='subquery',
    #     backref=db.backref('persons', lazy=True))

    def __repr__(self):
        return '<Hooman, id = %d, name = %s>' % (self.personId, self.personName)

attendees = db.Table('attendees',
    db.Column('foodId', db.ForeignKey('food.foodId'), primary_key=True),
    db.Column('attendeeId', db.ForeignKey('person.personId'), primary_key=True)
)

class Food(db.Model):
    foodId = db.Column(db.Integer, primary_key=True)
    cookId = db.Column(db.Integer, db.ForeignKey('person.personId'))
    locationLong = db.Column(db.Float)
    locationLat = db.Column(db.Float)
    price = db.Column(db.Integer)
    description = db.Column(db.String(2000))
    # attendees = db.relationship('Attendee', secondary=attendees, lazy

    def __repr__(self):
        return '<Fud, d = %d, cook = %d>' % (self.foodId, self.cookId)
   

class Feedback(db.Model):
    feedbackId = db.Column(db.Integer, primary_key=True)
    cookId = db.Column(db.Integer, db.ForeignKey('person.personId'))
    message = db.Column(db.String(2000))
    
feedbacks = db.Table('feedbacks',
    db.Column('feedbackId', db.ForeignKey('feedback.feedbackId'), primary_key=True),
    db.Column('personId', db.ForeignKey('person.personId'), primary_key=True)
)

class getAll(Resource):
    def get(self):
        pass
    def post(self):
        pass

api.add_resource(getAll, '/cook/all')

if __name__ == '__main__':
    app.run(debug=True)
