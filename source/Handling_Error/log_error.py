from ..tool.data_base_manage import ErrorDataBase
from pathlib import Path

from ..file_manage.jsonManager import *



error_datas_path = Path(r"source\handling_error\error_datas.json").absolute()
error_datas = load_from_json(error_datas_path)

class ErrorManager:
    def __init__(self, self_module):
        
        if os.path.exists(Path(r"source\handling_error\DBM_error").absolute()):
            pass
        
        self.db_path = Path(r"data\data_bases\error_log.db").absolute()

        # for debuging
        self.module = self_module

        self.db_manager = ErrorDataBase(self.db_path)
        
        self.update()
        
        
        
        
        
        
    def log(self, error_code):
        error_log_data = next((e for e in error_datas if e.get("errorid") == error_code), None)
         
        if not error_log_data or error_code == 10:
            self.db_manager.add({"errorid": 10, "error":f"unknown errorid [{self.module}]", "dangerlvl":2})
        else:
            self.db_manager.add(error_log_data)
        
        self.update()

    def shows(self) -> list:
        self.update()
        return []

    def _filter_errors(self, errors : list, mode):
        out_list = errors.copy()
        
        for error in errors:
            if error["dangerlvl"] < 3:
                out_list.remove(error)
            else:
                pass
        
    def update(self):
        self.db_manager.delete_timeup()

    def update_show(self, showed_errors: list):
        pass

    def finish(self):
        self.db_manager.connection.close()