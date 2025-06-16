from pathlib import Path

from .file_manage.jsonManager import *
from .run_proccess import RunEffect
from .file_manage.getImgpaths import available_types

from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMainWindow

from PyQt5.QtCore import Qt

from .window_ui import Ui_MainWindow

desktop = str(Path.home() / "Desktop")

empty_data1 = {
    "path": ""
}

empty_data2 = {
    "mode": "file",
    "copy": True
}


json_target_path = Path(r"data\export_data\target_path.json").absolute()
json_mode_path = Path(r"data\export_data\mode.json").absolute()
save_to_json(empty_data1, json_target_path)
save_to_json(empty_data2, json_mode_path)


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
        self.ui.gray_scale_b.clicked.connect(lambda: self.set_effect("gray_scale"))
        self.ui.negate_b.clicked.connect(lambda: self.set_effect("negate"))
        self.ui.vintage_b.clicked.connect(lambda: self.set_effect("vintage"))
        self.ui.mosaic_b.clicked.connect(lambda: self.set_effect("mosaic"))
        self.ui.oil_b.clicked.connect(lambda: self.set_effect("oil"))

        self.open_mode = "file"
        self.copy = True
        
        self.ui.copy_files_check.stateChanged.connect(self.update_copy_mode)

        self.import_button = self.ui.import_button
        self.import_button.clicked.connect(self.get_file)

        self.image_radiobutton = self.ui.image_i
        self.dir_radiobutton = self.ui.dir_i
        self.image_radiobutton.setChecked(True)

        self.image_radiobutton = self.ui.image_i.toggled.connect(
            lambda: self.change_mode("file"))
        self.dir_radiobutton = self.ui.dir_i.toggled.connect(
            lambda: self.change_mode("directory"))

        self.update_export()
        self.ui.retranslateUi(self.window)

    def update_copy_mode(self, state):
        if state == Qt.Checked:
            self.copy = True
        else:
            self.copy = False

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
        mode_dict = {
            "mode": self.open_mode,
            "copy": self.copy
        }
        
        save_to_json(mode_dict, json_mode_path)

        self.run_effect(self.current_effect)

    def change_mode(self, mode):
        self.open_mode = mode

    def get_file(self):
        path = self.open_dialog(self.window)

        if path:

            self.path_imported = True
            self.update_export()
            user_data_path = Path(r"user_data\user_data.json").absolute()
            user_data = load_from_json(user_data_path)

            if self.open_mode == "file":
                updated_user_data = {
                    "last_file": str(Path(path).parent),
                    "last_dir": user_data["last_dir"]
                }

            else:
                updated_user_data = {
                    "last_file": user_data["last_file"],
                    "last_dir": path
                }

            save_to_json(updated_user_data, user_data_path)

            saveDict = {"path": path}
            save_to_json(saveDict, json_target_path)


    def open_dialog(self, parent):
        user_data_path = Path(r"user_data\user_data.json").absolute()

        user_data = load_from_json(user_data_path)

        if self.open_mode == "file":
            if Path(user_data["last_file"]) == desktop:
                open_path = desktop

            elif check_path(user_data["last_file"]):
                open_path = user_data["last_file"]

            else:
                open_path = desktop

                fixed_user_data = {
                    "last_file": desktop,
                    "last_dir": user_data["last_dir"]
                }

                save_to_json(fixed_user_data, user_data_path)

            filter_text = f"Images ({" *" + " *".join(available_types)});;All Files (*)"

            dialog = QFileDialog(
                parent, directory=open_path, filter=filter_text)
            dialog.setFileMode(QFileDialog.ExistingFile)

            dialog.setWindowTitle("select file")

        elif self.open_mode == "directory":
            if Path(user_data["last_dir"]) == desktop:
                open_path = desktop

            elif check_path(user_data["last_dir"]):
                open_path = user_data["last_dir"]

            else:
                open_path = desktop

                fixed_user_data = {
                    "last_file": user_data["last_file"],
                    "last_dir": desktop
                }

                save_to_json(fixed_user_data, user_data_path)

            dialog = QFileDialog(parent, directory=open_path)

            dialog.setFileMode(QFileDialog.Directory)

            dialog.setWindowTitle("select file directories")

        else:
            raise ValueError("invalid open mode")

        if dialog.exec_():

            return dialog.selectedFiles()[0]

        return ""


def check_path(path):
    if os.access(path, os.R_OK) and os.access(path, os.F_OK):
        return True
    return False
