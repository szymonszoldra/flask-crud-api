from database import Database
from os import getenv
from dotenv import load_dotenv
from flask import Flask, request, jsonify
app = Flask(__name__)
load_dotenv()


@app.route('/')
def hello_world():
    return '''/setup - initialize table students in database
/create - add student in database
/read/id - show the record of the particular student with the given ID
/update/id - update particular student
/delete/id - delete particular student
'''


@app.route('/setup')
def setup_database():
    db_name = getenv('DB_NAME')
    db = Database(db_name)
    db.initialize('CREATE TABLE students (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, surname TEXT, mark INTEGER)')
    return 'Initialized table students in database'


@app.route('/create', methods=['POST'])
def create():
    req = request.get_json()
    db_name = getenv('DB_NAME')
    db = Database(db_name)
    name = req['name']
    surname = req['surname']
    mark = req['mark']

    query = 'INSERT INTO students (id ,name, surname, mark) VALUES (?,?,?,?)'
    db.create(query, name, surname, mark)
    return 'Insertion complete'


@app.route('/read/<student_id>')
def read(student_id):
    db_name = getenv('DB_NAME')
    db = Database(db_name)
    query = 'SELECT name, surname, mark FROM students WHERE id=?'
    student = db.read(query, student_id)
    return jsonify(student)

