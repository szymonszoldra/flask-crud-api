from database import Database
from os import getenv
from dotenv import load_dotenv
from flask import Flask
app = Flask(__name__)
load_dotenv()


@app.route('/')
def hello_world():
    return '''/setup - initialize table students in database
/create - add student in database
/read - show particular student record
/update - update particular student
/delete - delete particular student
'''


@app.route('/setup')
def setup_database():
    name = getenv('DB_NAME')
    db = Database(name)
    db.initialize('CREATE TABLE students (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, surname TEXT, mark INTEGER)')
    return 'Initialized table students in database'
