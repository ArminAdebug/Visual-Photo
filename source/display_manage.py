from pathlib import Path

from .file_manage.jsonManager import *
from .run_proccess import RunEffect
from .file_manage.getImgpaths import available_types

from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMainWindow

from .window_ui import Ui_MainWindow

empty_data = {
    "mode": "file",
    "path": ""
}
json_target_path = Path(r"data\TargetPath.json").absolute()
save_to_json(empty_data, json_target_path)


class DisplayManage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.open_mode = "file"
        


        self.import_button = self.ui.import_button
        self.import_button.clicked.connect(self.get_file)

        self.get_file()
        self.ui.retranslateUi(self)
        
    def update_open_mode(mode):
        pass

    def effect(self, name):
        self.run_effect(name)

    def get_file(self):
        path = self.open_dialog(self)

        if path:
            saveDict = {"mode": self.open_mode, "path": path}
            save_to_json(saveDict, json_target_path)

    def open_dialog(self, parent):

        if self.open_mode == "file":
            filter_text = f"Images ({" *" + " *".join(available_types)});;All Files (*)"

            dialog = QFileDialog(parent, filter=filter_text)
            print(type(filter_text))
            dialog.setFileMode(QFileDialog.ExistingFile)

            dialog.setWindowTitle("select file")

        elif self.open_mode == "directory":
            dialog = QFileDialog(parent)

            dialog.setFileMode(QFileDialog.Directory)

            dialog.setWindowTitle("select file directories")

        else:
            raise ValueError("invalid open mode")

        if dialog.exec_():

            return dialog.selectedFiles()[0]

        return ""
