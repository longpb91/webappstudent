from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy(app)

class Students(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    class_ = db.Column(db.String(200))
    subject = db.Column(db.Text())

    def __init__(self, id, name, class_, subject):
        self.id = id
        self.name = name
        self.class_ = class_
        self.subject = subject

        