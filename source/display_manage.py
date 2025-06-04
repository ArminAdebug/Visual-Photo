from pathlib import Path

from .file_manage.jsonManager import *
from .run_proccess import RunEffect
from .file_manage.getImgpaths import available_types

from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMainWindow

from .window_ui import Ui_MainWindow


desktop = Path.home() / 'Desktop'

empty_data = {
    "mode": "file",
    "path": ""
}
json_target_path = Path(r"data\TargetPath.json").absolute()
save_to_json(empty_data, json_target_path)



class DisplayManage:
    def __init__(self):
        super().__init__()
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        
        self.run_effect = RunEffect()
        self.path_imported = False
        self.effect_selected = False

        self.export_button = self.ui.export_button
        self.export_button.clicked.connect(self.effect)

        self.current_effect = ""

        self.ui.Blur_b.clicked.connect(lambda: self.set_effect("blur"))
        self.ui.glow_b.clicked.connect(lambda: self.set_effect("glow"))
        self.ui.gray_scale_b.clicked.connect(
            lambda: self.set_effect("gray_scale"))
        self.ui.negate_b.clicked.connect(lambda: self.set_effect("negate"))
        self.ui.vintage_b.clicked.connect(lambda: self.set_effect("vintage"))
        self.ui.mosaic_b.clicked.connect(lambda: self.set_effect("mosaic"))
        self.ui.oil_b.clicked.connect(lambda: self.set_effect("oil"))

        self.open_mode = "file"

        self.import_button = self.ui.import_button
        self.import_button.clicked.connect(self.get_file)
        
        self.image_radiobutton = self.ui.image_i
        self.dir_radiobutton = self.ui.dir_i
        self.image_radiobutton.setChecked(True)
        
        self.image_radiobutton = self.ui.image_i.toggled.connect(lambda: self.change_mode("file"))
        self.dir_radiobutton = self.ui.dir_i.toggled.connect(lambda: self.change_mode("directory"))
        
        self.update_export()        
        self.ui.retranslateUi(self.window)

    def update_open_mode(self, mode):
        pass

    def update_export(self):      
        if self.path_imported and self.effect_selected:
            self.export_button.setEnabled(True)

        else:
            self.export_button.setEnabled(False)

    def set_effect(self, name):
        self.current_effect = name
        self.effect_selected = True
        self.update_export()

    def effect(self):
        self.run_effect(self.current_effect)

    def change_mode(self, mode):
        self.open_mode = mode

    def get_file(self):
        path = self.open_dialog(self.window)

        if path:
            self.path_imported = True
            self.update_export()
            saveDict = {"mode": self.open_mode, "path": path}
            save_to_json(saveDict, json_target_path)

    def open_dialog(self, parent):

        if self.open_mode == "file":
            filter_text = f"Images ({" *" + " *".join(available_types)});;All Files (*)"

            dialog = QFileDialog(parent, filter=filter_text)
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
