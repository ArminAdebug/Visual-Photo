from ..tool.data_base_manage import ErrorDataBase
from pathlib import Path
import inspect

from ..file_manage.jsonManager import *



error_datas_path = Path(r"source\handling_error\error_datas.json").absolute()
error_datas = load_from_json(error_datas_path)

class ErrorManager:
    def __init__(self, self_module):
        self.db_path = Path(r"data\data_bases\error_log.db").absolute()

        # for debuging
        self.module = self_module

        self.db_manager = ErrorDataBase(self.db_path)
        
    def log(self, error_code):
        error_log_data = next((e for e in error_datas if e.get("errorid") == error_code), None)
         
        if not error_log_data or error_code == 10:
            self.db_manager.add({"error":f"unknown error code [{self.module}]", "errorid": 10, "dangerlvl":2})
        else:
            self.db_manager.add(error_log_data)
        

    def shows(self) -> list:
        return []

    def _filter_errors(self, data, mode):
        pass

    def update_show(self, showed_errors: list):
        pass

    def finish(self):
        self.db_manager.connection.close()