# Flask CRUD API

Simple CRUD API written in Python with Flask microframework and SQLite database.

## Installation

On Linux

```shell script
git clone https://github.com/szymonszoldra/flask-crud-api.git
cd flask-crud-api
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

On Windows
```shell script
git clone https://github.com/szymonszoldra/flask-crud-api.git
cd flask-crud-api
py -3 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Make .env file with DB_NAME=name_of_your_db.sqlite3, just like in .env.example

Then write in terminal:

```shell script
export FLASK_APP=server.py
export FLASK_ENV=development
flask run
```

App will start by default on http://127.0.0.1:5000/
## Usage

You can use program like POSTMAN, or make requests with programming language.

Endpoints:
* / - displays commands below (GET)
* /setup - initialize table students in database (GET)
* /create - add student to database (POST)
* /read/id - show the record of the particular student with the given ID (GET)
* /update/id - update particular student (PUT)
* /delete/id - delete particular student (DELETE)


### Setup
Make GET request to /setup to initialize Database with the students table.

### Create
Make POST request with JSON body like below to /create, where X is string and Y is integer.
```json
{
  "name": "X",
  "surname": "X",
  "mark": Y
}
```

### Read
Make GET request to /read/id with the ID of the student, id must be an integer.

### Update
Make PUT request to /update/id with the ID of the student with JSON body like below, id must be an integer.
```json
{
    "mark":4
}
```

### Delete
Make DELETE request to /delete/id with the ID of the student, id must be an integer.


