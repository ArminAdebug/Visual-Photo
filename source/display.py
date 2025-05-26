import sys
import os
from pathlib import Path
from .customWidgets import CustumWidgets
from .file_manage.jsonManager import *
from .run_proccess import RunEffect
import subprocess

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

        self.window.setLayout(self.main_layout)

        self.jsonTargetPath = _get_full_path(Path(r"data\TargetPath.json"))

        self.label = self.Cwidgets.Label(
            "Choice Effect", self.window, (900, -60), 40)

        self.button1 = self.Cwidgets.button(self.window,"1", pos=(860, -50), size=(500, 100))
        self.button1.clicked.connect(lambda: self.get_file("directory"))

        self.button2 = self.Cwidgets.button(self.window, "2", (860, -50), (500, 100), "#40f411")
        self.button2.clicked.connect(lambda: self.apply_effect("gray_scale"))

        self.Cwidgets.add_Layout(self.button1, self.main_layout)
        self.Cwidgets.add_Layout(self.button2, self.main_layout)
        self.Cwidgets.add_Layout(self.label, self.main_layout)
        

        self.window.show()

        sys.exit(self.Cwidgets.app.exec_())

    def get_file(self, mode):
        path = self.Cwidgets.open_dialog(self.window, mode=mode)

        if path:
            saveDict = {"mode": "file","path": path}
            save_to_json(saveDict, self.jsonTargetPath)

    def apply_effect(self, name):
        pass
        #run = RunEffect()
        
        #run.run(name)
        

    


