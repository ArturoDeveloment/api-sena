import sqlite3
from pathlib import Path

class Conexion:
    conetion = None
    database_file = None

    def __init__(self):
        self.conection = sqlite3.connect("info_sena.db")
        self.database_file = str(Path(__file__).parent.parent.joinpath('info_sena.db'))
    
    def create_table(self, table: str, columns: list):
        columns_into = ",".join([i for i in columns])
        self.execute_commit([f"CREATE table {table} ({columns_into})"])


    def execute_commit(self, query):
        with sqlite3.connect(self.database_file) as conn:
            try:
                cursor = conn.cursor()
                cursor = cursor.execute(*query)
                conn.commit()
                print(f"Se guardo el query")
            except sqlite3.OperationalError:
                print("No se guardo el query")
            return cursor
            