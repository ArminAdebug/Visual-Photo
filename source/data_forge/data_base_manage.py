import sqlite3
from datetime import datetime

class DataBaseManager:
    def __init__(self, data_base_path, table_base : dict):
        self.connection = sqlite3.connect(data_base_path)
        self.cursor = self.connection.cursor()

        self.table_name = table_base["table name"]

        table = ""
        if table_base["subject"] == "errorlog":
            table = """            
                error TEXT NOT NULL,
                errorcode NOT NULL,
                dangerlvl NOT NULL,
                date TEXT NOT NULL
            """
        
        self.cursor.execute(F"""CREATE TABLE IF NOT EXISTS {self.table_name} ({table})""")
        
        self.connection.commit()
        
    def write(self, *data):
        date = datetime.now()
        date = date.strftime("%Y#%m#%d#%H#%M#%S")
        print(date)
        
        self.cursor.execute(f"INSERT INTO {self.table_name} (error, errorcode, dangerlvl, date) VALUES (?, ?, ?, ?)", [*data, date])
        
        self.connection.commit()

    def read(self, locate):
        pass

    def search(self, target):
        pass
