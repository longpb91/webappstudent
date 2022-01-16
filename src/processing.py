from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy(app)


def get_data_query(query):
    results = db.session.execute(query)
    lst = []
    for r in results:
        lst.append(r)
    return lst


def convert_list_to_string(lst):
    s = ''
    count = 0
    for l in lst:
        count += 1
        if count < len(lst):
            s += str(l) + ', '
        elif count >= len(lst):
            s += str(l)
    return s

