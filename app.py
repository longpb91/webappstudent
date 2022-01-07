from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os

# from src.models import Students

# from dotenv import load_dotenv
#
#
# load_dotenv()

app = Flask(__name__)

# ENV = 'dev'
ENV = 'prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL_DEV')
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL_PROD')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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


@app.route('/')
def main_page():
    return render_template('test_mainpage.html')


@app.route('/students', methods=['GET', 'POST'])
def add_students():
    try:
        if request.method == 'POST':
            id = request.form['studentid']
            name = request.form['name']
            class_ = request.form['classes']
            subject = request.form.getlist('subject')

            if id == "" or name == "" or class_ == "" or subject == "":
                return render_template("students.html", message='Please enter required fields.')

            # if len(id) < 12 or len(id) > 12:
            #     return render_template("students.html", message='The id must contain 12 numbers.')

            if id.isdigit() is False:
                return render_template("students.html", message='Only enter number!')

            if db.session.query(Students).filter(Students.id == id).count() == 0:
                data_students = Students(id, name, class_, subject)
                db.session.add(data_students)
                db.session.commit()

                # return "Student with ID={}".format(data_students.id)
                return render_template("success.html")
            return render_template('students.html', message='You have already submitted.')
        return render_template("students.html")
    except Exception as e:
        return(str(e))


if __name__ == '__main__':
    # app.debug = True
    app.run()

