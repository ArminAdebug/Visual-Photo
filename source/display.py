import sys
import os
from pathlib import Path
from .customWidgets import CustumWidgets
from .file_manage.jsonManager import *


current_dir = os.path.dirname(__file__)


def _get_full_path(path):
    file_path = os.path.join(current_dir, "..", path)
    file_path = os.path.abspath(file_path)
    return file_path


class Display:
    def __init__(self):
        self.Cwidgets = CustumWidgets()
        self.window = self.Cwidgets.setupWindow()

        self.main_layout = self.Cwidgets.create_layout(layout_type="grid")
        self.scroll = self.Cwidgets.vertical_scroll()
        
        self.window.setLayout(self.main_layout)

        self.jsonTargetPath = _get_full_path(Path(r"data\TargetPath.json"))

        self.label = self.Cwidgets.Label("Choice Effect", self.window, (860, 10), 40)

        self.button = self.Cwidgets.button(self.window, pos=(860, 0), size=(500, 100))
        self.button.clicked.connect(lambda: self.get_file("directory"))
        
        self.Cwidgets.add_Layout(self.label, self.main_layout)         
        self.scroll.addWidget(self.button)        
      
        self.window.show()
        

        sys.exit(self.Cwidgets.app.exec_())

    def get_file(self, mode):
        path = self.Cwidgets.open_dialog(self.window, mode=mode)

        if path:
            saveDict = {"mode": "file",
                        "path": path}
            save_to_json(saveDict, self.jsonTargetPath)

    def apply_effect(self, name):
        pass