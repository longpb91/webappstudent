from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
# import traceback

from src.models import Students, Classes, Teachers, Subjects
from src.processing import convert_list_to_string, get_data_query

from dotenv import load_dotenv


load_dotenv()

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
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SESSION_TYPE'] = 'filesystem'


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
        query_1 = 'SELECT classname FROM add_classes'
        results = db.session.execute(query_1)
        lst = []
        for r in results:
            lst.append(r[0])

        if request.method == 'POST':
            if request.form['service'] == 'add':
                name = request.form['studentname']
                gender = request.form['studentgender']
                class_ = request.form['classes']
                if name == "" or class_ == "" or gender == "":
                    error = "Please enter required fields."
                    return render_template("students.html", lst=lst, error=error)

                data_students = Students(name, gender, class_)
                db.session.add(data_students)
                db.session.commit()

                query_5 = f"SELECT * FROM add_students"
                data = tuple(get_data_query(query_5))

                msg = 'Success! Thank you for your information.'
                return render_template('students.html', lst=lst, msg=msg, data_all=data)

            elif request.form['service'] == 'search':
                name = request.form['getstudentname']

                query_2 = f"SELECT * FROM add_students WHERE studentname = '{name}'"
                lst_data = get_data_query(query_2)

                if len(lst_data) >= 1:
                    headings = ('StudentID', 'StudentName', 'Gender', 'Class')
                    data = tuple(lst_data)
                    msg = 'Success!'
                    return render_template('students.html', lst=lst, headings=headings, data=data, msg=msg)
                else:
                    error = 'Student not found! Please try again!'
                    return render_template('students.html', lst=lst, error=error,)

            elif request.form['service'] == 'delete':
                id_ = request.form['delete_id']
                query_3 = f"DELETE FROM add_students WHERE studentid='{id_}'"
                db.session.execute(query_3)
                db.session.commit()
                msg = f"Delete Student with id = {id_} successfully!"
                return render_template('students.html', lst=lst, msg=msg)

            elif request.form['service'] == 'show':
                query_4 = f"SELECT * FROM add_students"
                lst_data = get_data_query(query_4)

                if len(lst_data) > 0:
                    data = tuple(lst_data)
                    msg = 'Success!'
                    return render_template('students.html', lst=lst, data_all=data, msg=msg)
                else:
                    error = 'Student not found! Please try again!'
                    return render_template('students.html', lst=lst, error=error)

        return render_template("students.html", lst=lst)
    except Exception as e:
        return str(e)
        # return traceback.print_exc()


@app.route('/edit_students', methods=['GET', 'POST'])
def edit_students():
    try:
        if request.method == 'POST':
            id_ = request.form['editid']
            if request.form['service'] == 'editsuccess':
                name = request.form['studentname']
                gender = request.form['studentgender']
                class_ = request.form['classes']

                if name == "":
                    query_student = f"SELECT * FROM add_students WHERE studentid={id_}"
                    lst_student = get_data_query(query_student)
                    query_class = 'SELECT classname FROM add_classes'
                    lst_class = get_data_query(query_class)
                    error = "Please enter required fields."
                    return render_template("edit_students.html", lst_student=lst_student[0],
                                           lst_class=lst_class, error=error)

                query_update = f"UPDATE add_students " \
                               f"SET studentname='{name}', studentgender='{gender}', class_='{class_}' " \
                               f"WHERE studentid = {id_}"

                db.session.execute(query_update)
                db.session.commit()

                flash('Updated', 'success')
                return redirect(url_for('add_students'))
                # return print(type(id_))
            elif request.form['service'] == 'editstudent':
                query_student = f"SELECT * FROM add_students WHERE studentid={id_}"
                lst_student = get_data_query(query_student)
                query_class = 'SELECT classname FROM add_classes'
                lst_class = get_data_query(query_class)
                return render_template('edit_students.html', lst_class=lst_class, lst_student=lst_student[0])
    except Exception as e:
        return str(e)
        # return traceback.print_exc()


@app.route('/teachers', methods=['GET', 'POST'])
def add_teachers():
    try:
        query_1 = 'SELECT classname FROM add_classes'
        results = db.session.execute(query_1)
        lst_classes = []
        for r in results:
            lst_classes.append(r[0])

        if request.method == 'POST':
            if request.form['service'] == 'add_teacher':
                teachername = request.form['teacher']
                teachergender = request.form['teacher_gender']
                classes = request.form.getlist('teacher_classes')
                classes_ = convert_list_to_string(classes)

                if teachername == '':
                    error = "Please enter required fields."
                    return render_template("teacher_add.html", lst_classes=lst_classes, error=error)

                data_teacher = Teachers(teachername, teachergender, classes_)
                db.session.add(data_teacher)
                db.session.commit()

                query_all = "SELECT * FROM add_teachers"
                data_all = get_data_query(query_all)

                msg = 'Successfully! Thank you for your information.'
                return render_template("teacher_add.html", msg=msg, lst_classes=lst_classes, data_all=data_all)

            elif request.form['service'] == 'search_teacher':
                teacher_name = request.form['getteachername']
                query_2 = f"SELECT * FROM add_teachers WHERE teachername='{teacher_name}'"
                lst_data = get_data_query(query_2)
                if len(lst_data) >= 1:
                    headings = ('Teacher_ID', 'Full_Name', 'Gender', 'Classes_in_charge')
                    data = tuple(lst_data)
                    msg = "Success!"
                    return render_template('teacher_add.html', lst_classes=lst_classes, headings=headings,
                                            data=data, msg=msg)

                else:
                    error = 'Teacher not found! Please try again!'
                    return render_template('teacher_add.html', lst_classes=lst_classes, error=error)

            elif request.form['service'] == 'delete_teacher':
                delete_tid = request.form['delete_tid']
                query_delete = f"DELETE FROM add_teachers WHERE teacherid='{delete_tid}'"
                db.session.execute(query_delete)
                db.session.commit()
                msg = f"Delete teacher with id = {delete_tid} successfully!"
                return render_template('teacher_add.html', lst_classes=lst_classes, msg=msg)

            elif request.form['service'] == 'show_teachers':
                query_3 = "SELECT * FROM add_teachers"
                lst_data_all = get_data_query(query_3)
                data_all = tuple(lst_data_all)
                msg = "Success!"
                return render_template('teacher_add.html', data_all=data_all, msg=msg, lst_classes=lst_classes)

        return render_template('teacher_add.html', lst_classes=lst_classes)
    except Exception as e:
        return str(e)


@app.route('/edit_teacher', methods=['GET', 'POST'])
def edit_teacher():
    try:
        if request.method == 'POST':
            teacher_id = request.form['edit_id']
            if request.form['service'] == 'edit_teacher':
                query_teacher = f"SELECT * FROM add_teachers WHERE teacherid={teacher_id}"
                lst_teacher = get_data_query(query_teacher)
                query_class = f"SELECT classname from add_classes"
                lst_classes = get_data_query(query_class)
                return render_template('edit_teacher.html', lst_teacher=lst_teacher[0], lst_classes=lst_classes)
            elif request.form['service'] == 'edit_success':
                teacher_name = request.form['teacher']
                teacher_gender = request.form['teacher_gender']
                classes = convert_list_to_string(request.form.getlist('teacher_classes'))

                if teacher_name == "":
                    query_teacher = f"SELECT * FROM add_teachers WHERE teacherid={teacher_id}"
                    lst_teacher = get_data_query(query_teacher)
                    query_class = f"SELECT classname from add_classes"
                    lst_classes = get_data_query(query_class)
                    error = "Please enter required fields."
                    return render_template("edit_teacher.html", lst_teacher=lst_teacher[0],
                                           lst_classes=lst_classes, error=error)

                query_update = f"UPDATE add_teachers " \
                               f"SET teachername='{teacher_name}', teachergender='{teacher_gender}'," \
                               f"teacherclasses='{classes}'" \
                               f"WHERE teacherid = {teacher_id}"
                db.session.execute(query_update)
                db.session.commit()

                flash('Updated', 'success')
                return redirect(url_for('add_teachers'))
            elif request.form['service'] == 'cancel':
                # flash('Canceled edit!', 'danger')
                return redirect(url_for('add_teachers'))
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
    # app.secret_key = os.environ.get('SECRET_KEY')
    app.run()
