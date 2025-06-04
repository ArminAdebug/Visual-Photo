from pathlib import Path
from .file_manage.jsonManager import *
from .run_proccess import RunEffect

from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMainWindow, QApplication

from .window_ui import Ui_MainWindow

empty_data = {
    "mode":"file",
    "path":""
}
json_data_path = Path(r"data\TargetPath.json").absolute()
save_to_json(empty_data, json_data_path)



class DisplayManage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.open_mode = "file"
        
        self.import_button = self.ui.import_button
        self.import_button.clicked.connect(self.get_file)
        
        self.get_file()
        
    def update_open_mode(mode):
        pass
    
    def effect(self, name):
        self.run_effect(name)        

    def get_file(self):
        path = self.open_dialog(self)

        if path:
            saveDict = {"mode": "file","path": path}
            save_to_json(saveDict, self.jsonTargetPath)

    def open_dialog(self, parent):
        dialog = QFileDialog(parent)
        dialog.setWindowTitle("select file" if self.open_mode == "file" else "select file directories")

        if self.open_mode == "file":
            dialog.setFileMode(QFileDialog.ExistingFile)

        elif self.open_mode == "directory":

            dialog.setFileMode(QFileDialog.Directory)
        if dialog.exec_():

            return dialog.selectedFiles()[0]

        return ""
    


