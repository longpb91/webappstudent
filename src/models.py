from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy(app)


class Students(db.Model):
    __tablename__ = 'add_students'
    studentid = db.Column(db.Integer, primary_key=True)
    studentname = db.Column(db.String(200))
    class_ = db.Column(db.String(200))

    def __init__(self, studentname, class_):
        self.studentname = studentname
        self.class_ = class_


class Classes(db.Model):
    __tablename__ = 'add_classes'
    classid = db.Column(db.String, primary_key=True)
    classname = db.Column(db.String(200))

    def __init__(self, classid, classname):
        self.classid = classid
        self.classname = classname


class Teachers(db.Model):
    __tablename__ = 'add_teachers'
    teacherid = db.Column(db.Integer, primary_key=True)
    teachername = db.Column(db.String(200))

    def __init__(self, teachername):
        self.teachername = teachername


class Subjects(db.Model):
    __tablename__ = 'add_subjects'
    subjectid = db.Column(db.String(10), primary_key=True)
    subjectname = db.Column(db.String(200))

    def __init__(self, subjectid, subjectname):
        self.subjectid = subjectid
        self.subjectname = subjectname

