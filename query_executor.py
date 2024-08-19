import sqlite3
import mysql.connector
import psycopg2

class QueryExecutor:
    def __init__(self, db_type, connection_params):
        self.db_type = db_type
        self.connection_params = connection_params
        self.connection = None

    def connect(self):
        if self.db_type == 'sqlite':
            self.connection = sqlite3.connect(**self.connection_params)
        elif self.db_type == 'mysql':
            self.connection = mysql.connector.connect(**self.connection_params)
        elif self.db_type == 'postgresql':
            self.connection = psycopg2.connect(**self.connection_params)
        else:
            raise ValueError(f"Unsupported database type: {self.db_type}")

    def execute_query(self, query):
        if not self.connection:
            self.connect()
        
        cursor = self.connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return results

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None

