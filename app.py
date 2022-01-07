from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os

# from dotenv import load_dotenv


# load_dotenv()

app = Flask(__name__)

# db = SQLAlchemy(app)


@app.route('/')
def main_page():
    return render_template('test_mainpage.html')

@app.route('/students')
def students():
    return render_template('students.html')



if __name__ == '__main__':
    app.debug = True
    app.run()

