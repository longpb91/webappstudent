from flask_sqlalchemy import SQLAlchemy
from src.app import app

app_model = app

db = SQLAlchemy(app_model)


class Students(db.Model):
    __tablename__ = 'add_students'
    studentid = db.Column(db.Integer, primary_key=True)
    studentname = db.Column(db.String(200))
    studentgender = db.Column(db.String(10))
    class_ = db.Column(db.String(200))

    def __init__(self, studentname, studentgender, class_):
        self.studentname = studentname
        self.studentgender = studentgender
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
    teachergender = db.Column(db.String(10))
    teacherclasses = db.Column(db.String(1000))
    teachsubject = db.Column(db.String(200))

    def __init__(self, teachername, teachergender, teacherclasses, teachsubject):
        self.teachername = teachername
        self.teachergender = teachergender
        self.teacherclasses = teacherclasses
        self.teachsubject = teachsubject


class Subjects(db.Model):
    __tablename__ = 'add_subjects'
    subjectid = db.Column(db.String(10), primary_key=True)
    subjectname = db.Column(db.String(200))

    def __init__(self, subjectid, subjectname):
        self.subjectid = subjectid
        self.subjectname = subjectname

db.create_all()
db.session.commit()


