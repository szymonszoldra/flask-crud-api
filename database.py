import sqlite3


class Database:
    def __init__(self, name):
        self.connection = sqlite3.connect(name)
        self.cursor = self.connection.cursor()

    def initialize(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def __del__(self):
        self.connection.close()
