from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
import traceback

from src.models import Students, Classes, Teachers, Subjects

from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)

ENV = 'dev'
# ENV = 'prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL_DEV')
else:
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL_PROD')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route('/')
def main_page():
    return render_template('mainpage.html')


@app.route('/classes', methods=['GET', 'POST'])
def add_classes():
    try:
        if request.method == 'POST':
            class_id = request.form['class_id']
            class_id = class_id.upper()
            print(class_id)
            class_name = request.form['classes']

            if class_id == "" or class_name == "":
                error = "Please enter required fields."
                return render_template('class_add.html', error=error)

            if len(class_id) < 5:
                error = "The ID must contain 5 characters."
                return render_template('class_add.html', error=error)

            if db.session.query(Classes).filter(Classes.classid == class_id).count() == 0:
                data_classes = Classes(class_id, class_name)
                db.session.add(data_classes)
                db.session.commit()

                msg = 'Successfully! Thank you for your information.'
                return render_template('class_add.html', msg=msg)
            error = 'You have already submitted.'
            return render_template('class_add.html', error=error)
        return render_template('class_add.html')
    except Exception as e:
        return str(e)
        # return traceback.print_exc()


@app.route('/students', methods=['GET', 'POST'])
def add_students():
    try:
        query = 'SELECT classname FROM add_classes'
        results = db.session.execute(query)
        lst = []
        for r in results:
            lst.append(r[0])

        if request.method == 'POST':
            name = request.form['studentname']
            class_ = request.form['classes']

            if name == "" or class_ == "":
                error = "Please enter required fields."
                return render_template("students.html", lst=lst, error=error)

            data_students = Students(name, class_)
            db.session.add(data_students)
            db.session.commit()

            # return "Student with ID={}".format(data_students.id)
            # return render_template("success.html")
            msg = 'Successfully! Thank you for your information.'
            return render_template('students.html', lst=lst, msg=msg)
        return render_template("students.html", lst=lst)
    except Exception as e:
        return str(e)
        # return traceback.print_exc()


@app.route('/students-info')
def get_students():
    return render_template('studentsinfo.html')


@app.route('/teachers', methods=['GET', 'POST'])
def add_teachers():
    try:
        if request.method == 'POST':
            teachername = request.form['teacher']

            if teachername == '':
                error = "Please enter required fields."
                return render_template("teacher_add.html", error=error)

            data_teacher = Teachers(teachername)
            db.session.add(data_teacher)
            db.session.commit()

            msg = 'Successfully! Thank you for your information.'
            return render_template("teacher_add.html", msg=msg)
        return render_template('teacher_add.html')
    except Exception as e:
        return str(e)


@app.route('/subjects', methods=['GET', 'POST'])
def add_subjects():
    try:
        if request.method == 'POST':
            subject_id = request.form['subjectid']
            subject_name = request.form['subjectname']

            if subject_id == '' or subject_name == '':
                error = "Please enter required fields."
                return render_template("subject_add.html", error=error)
            if db.session.query(Subjects).filter(Subjects.subjectid == subject_id).count() == 0:
                data_subject = Subjects(subject_id, subject_name)
                db.session.add(data_subject)
                db.session.commit()
                msg = 'Successfully! Thank you for your information.'
                return render_template('subject_add.html', msg=msg)
            error = 'You have already submitted.'
            return render_template('subject_add.html', error=error)
        return render_template('subject_add.html')
    except Exception as e:
        return str(e)



if __name__ == '__main__':
    # app.debug = True
    app.run()

