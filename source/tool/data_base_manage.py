import sqlite3
from datetime import datetime

from pathlib import Path

class ErrorDataBase:
    def __init__(self, data_base_path):
        self.connection = sqlite3.connect(data_base_path)
        self.cursor = self.connection.cursor()
        
        self.cursor.execute(F"""CREATE TABLE IF NOT EXISTS errorlog (
            error TEXT,
            errorid INTEGET PRIMSRY KEY,
            dangerlvl INTEGER NOT NULL,
            date TEXT DEFAULT CURRENT_TIMESTAMP,
            deley DEFAULT 0
            )""")
        
        self.connection.commit()
        
    def add(self, data : dict):

        for i in range(10):
            print(i)
            try:    
                self.cursor.execute(f"INSERT INTO errorlog {(*data.keys(),)} VALUES (?, ?, ?)", [*data.values()])

                self.connection.commit()
            except sqlite3.Error as e:
                if i == 9:
                    print(e)
            
            else:
                break
        else:
            # create critical file clue
            with open(Path(r"source\handling_error\c_error").absolute(), "w") as error_file:
                pass
            
    def read(self, where): 
        pass
  
    def search(self, where):
        pass
