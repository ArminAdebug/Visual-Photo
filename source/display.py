import sys
from .customWidgets import CustumWidgets
from .file_manage.jsonManager import *

import os
current_dir = os.path.dirname(__file__)


def _get_font_path(path):
    file_path = os.path.join(current_dir, "..", path)
    file_path = os.path.abspath(file_path)
    return file_path


class Display:
    def __init__(self):
        self.Cwidgets = CustumWidgets()
        self.window = self.Cwidgets.setupWindow()

        self.main_layout = self.Cwidgets.create_layout()

        self.window.setLayout(self.main_layout)

        self.jsonTargetPath = _get_font_path(r"data\TargetPath.json")

        self.label = self.Cwidgets.Label(
            "choice effect", self.window, (150, 350), 50)

        self.button = self.Cwidgets.create_button(self.window)
        self.button.clicked.connect(lambda: self.get_file("directory"))

        self.Cwidgets.add_Layout(self.button, self.main_layout)
        self.Cwidgets.add_Layout(self.label, self.main_layout)

        self.window.show()

        sys.exit(self.Cwidgets.app.exec_())

    def get_file(self, mode):
        path = self.Cwidgets.open_dialog(self.window, mode=mode)

        if path:
            self.label.setText(path)
            saveDict = {"mode": "file",
                        "path": path}
            save_to_json(saveDict, self.jsonTargetPath)




