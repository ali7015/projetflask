from flask_sqlalchemy import SQLAlchemy
from .views import app
import logging as lg
import enum

# Create database connection object
db = SQLAlchemy(app)

class Gender(enum.Enum):
    female= 0
    male=1
    other= 2


class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    gender = db.Column(db.Enum(Gender), nullable=False)

    def __init__(self, description, gender):
        self.description = description
        self.gender = gender

def init_db():
    db.drop_all()
    db.create_all()
    db.session.add(Content("Vous etes fort!!!", Gender['male']))
    db.session.add(Content("vous etes belle", Gender['female']))
    db.session.commit()
    lg.warning('Database initialized!')