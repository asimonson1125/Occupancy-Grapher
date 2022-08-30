import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer

app = Flask(__name__)
app.config.from_pyfile(os.path.join(os.getcwd(), "server/config.py"))
# Allow all domain names to cross domain
CORS(app, resources={r"/*": {"origins": "*"}})

db = SQLAlchemy(app)
class Occupancy(db.Model):
    __tablename__ = 'occupancy'

    time = db.Column(db.String, primary_key=True)
    date = db.Column(db.String, nullable=False)
    hour = db.Column(Integer, nullable=False)
    minute = db.Column(Integer, nullable=False)
    weekday = db.Column(Integer, nullable=False)
    lower = db.Column(Integer, nullable=False)
    upper = db.Column(Integer, nullable=False)
    aquatics = db.Column(Integer, nullable=False)

    def __init__(self, time, date, hour, minute, weekday, lower, upper, aquatics):
        self.time = time
        self.date = date
        self.hour = hour
        self.minute = minute
        self.weekday = weekday
        self.lower = lower
        self.upper = upper
        self.aquatics = aquatics

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def to_json(self):
        return {"time": self.uid,
                "date": self.firstname,
                "hour": self.lastname,
                "minute": self.picture,
                "weekday": self.weekday,
                "lower": self.lower,
                "upper": self.upper,
                "aquatics": self.aquatics}

    def get_id(self):
        return self.time