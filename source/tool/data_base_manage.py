import sqlite3
from datetime import datetime

from pathlib import Path

class ErrorDataBase:
    def __init__(self, data_base_path):
        self.connection = sqlite3.connect(data_base_path)
        self.cursor = self.connection.cursor()

        self.cursor.execute(F"""CREATE TABLE IF NOT EXISTS errorlog (
            errorid INTEGER PRIMARY KEY,
            error TEXT,
            dangerlvl INTEGER,
            date TEXT DEFAULT CURRENT_TIMESTAMP,
            delay INTEGER DEFAULT 0
            )""")
        
        self.cursor.execute("CREATE UNIQUE INDEX IF NOT EXISTS idx_errorid ON errorlog(errorid)")
        
        self.connection.commit()

    def add(self, data: dict):
        errorid = data["errorid"]
        error = data["error"]
        dangerlvl = data["dangerlvl"]
        
        for i in range(10):
            print(i + 1, end=" . ")
            try:
                self.cursor.execute(
                    f"""INSERT INTO errorlog (errorid, error, dangerlvl) VALUES (?, ?, ?)
                    ON CONFLICT(errorid) DO UPDATE SET date = CURRENT_TIMESTAMP
                    """, (errorid, error, dangerlvl))

                self.connection.commit()
            except sqlite3.Error as e:
                self.connection.rollback()
                
                if i == 9:
                    print() 
                    print(e)

            else:
                break
           
        else:
            # create critical file clue
            with open(Path(r"source\handling_error\DBM_error").absolute(), "w") as error_file:
                pass

    def delete(self, errorid : int):
        self.cursor.execute("delete from errorlog where errorid = ?", (errorid, ))

        self.connection.commit()

    def delete_timeup(self):
        self.cursor.execute("delete from errorlog where ((julianday(CURRENT_TIMESTAMP) - julianday(date))) * 24 * 60 > 2")

        self.connection.commit()

    def read(self, where):
        pass

    def search(self, where):
        pass
