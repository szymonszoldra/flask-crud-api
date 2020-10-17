import sqlite3


class Database:
    def __init__(self, name):
        self.connection = sqlite3.connect(name)
        self.cursor = self.connection.cursor()

    def initialize(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except sqlite3.Error as e:
            print(e)

    def create(self, query, name, surname, mark):
        try:
            self.cursor.execute(query, (None, name, surname, mark))
            self.connection.commit()
        except sqlite3.Error as e:
            print(e)

    def read(self, query, student_id):
        try:
            if type(int(student_id[0])) == str:
                raise ValueError
            query = self.cursor.execute(query, student_id)
            self.connection.commit()
            return query.fetchall()
        except sqlite3.Error as e:
            return {'error': str(e)}
        except ValueError:
            return {'error': 'ID must be an integer'}

    def update(self, query, student_info):
        try:
            self.cursor.execute(query, student_info)
            self.connection.commit()
        except sqlite3.Error as e:
            print(e)

    def __del__(self):
        self.connection.close()
