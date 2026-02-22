import sqlite3

class DatabaseAdapter:
    def __init__(self, db_path):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

    def select_with_condition(self, columns, table, condition):
        query = f"SELECT {columns} FROM {table}"
        if condition:
            query += f" WHERE {condition}"
        self.cursor.execute(query)

    def insert(self, table, data):
        columns = ", ".join(data.keys())
        placeholders = ", ".join("?" for _ in data)
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        self.cursor.execute(query, tuple(data.values()))
        self.connection.commit()

    def get_one(self):
        val = self.cursor.fetchone()
        self.connection.commit()
        return val
