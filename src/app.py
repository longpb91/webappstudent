from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
import traceback

from src.models import Students

# from dotenv import load_dotenv


# load_dotenv()

app = Flask(__name__)

# ENV = 'dev'
ENV = 'prod'

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


@app.route('/students', methods=['GET', 'POST'])
def add_students():
    try:
        if request.method == 'POST':
            id = request.form['studentid']
            name = request.form['name']
            class_ = request.form['classes']
            subject = request.form.getlist('subject')

            if id == "" or name == "" or class_ == "" or subject == "":
                error = "Please enter required fields."
                return render_template("students.html", error=error)

            if len(id) < 5 or len(id) > 5:
                error = "The id must contain 12 numbers."
                return render_template("students.html", error=error)
                # return render_template("students.html", message='The id must contain 12 numbers.')

            if id.isdigit() is False:
                error = "Only enter number in Student ID"
                return render_template("students.html", error=error)
                # return render_template("students.html", message='Only enter number!')

            if db.session.query(Students).filter(Students.id == id).count() == 0:
                data_students = Students(id, name, class_, subject)
                db.session.add(data_students)
                db.session.commit()

                # return "Student with ID={}".format(data_students.id)
                # return render_template("success.html")
                msg = 'Successfully! Thank you for your information.'
                return render_template('students.html', msg=msg)
            error = 'You have already submitted.'
            return render_template('students.html', error=error)
        return render_template("students.html")
    except Exception as e:
        # return(str(e))
        return traceback.print_exc()


@app.route('/students-info')
def get_students():
    return render_template('studentsinfo.html')


if __name__ == '__main__':
    # app.debug = True
    app.run()
