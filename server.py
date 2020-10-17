from database import Database
from os import getenv
from dotenv import load_dotenv
from flask import Flask, request, jsonify
app = Flask(__name__)
load_dotenv()


@app.route('/')
def hello_world():
    return '''/setup - initialize table students in database
/create - add student to database
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
    student = db.read(query, (student_id,))
    return jsonify(student)


@app.route('/update/<student_id>', methods=['PUT'])
def update(student_id):
    req = request.get_json()
    db_name = getenv('DB_NAME')
    db = Database(db_name)
    new_mark = req['mark']
    query = 'UPDATE students SET mark=? WHERE id=?'
    db.update(query, (new_mark, student_id))
    return 'Updated successfully'


@app.route('/delete/<student_id>', methods=['DELETE'])
def delete(student_id):
    db_name = getenv('DB_NAME')
    db = Database(db_name)
    query = 'DELETE FROM students WHERE id=?'
    db.delete(query, (student_id,))
    return 'Deleted successfully'
