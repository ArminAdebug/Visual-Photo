import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QInputDialog
import time
from customWidgets import CustumWidgets
from jsonManager import *


class App:
    def __init__(self):
        self.Cwidgets = CustumWidgets()
        self.window = self.Cwidgets.setupWindow()

        self.main_layout = self.Cwidgets.create_layout()

        self.window.setLayout(self.main_layout)

        self.jsonTargetPath = "TargetPath.json"

        self.label = self.Cwidgets.Label(
            "choice effect", self.window, (150, 350), 50)
        
        self.button = self.Cwidgets.create_button(self.window)
        
        def on_button_click():
            path = self.Cwidgets.open_dialog()
            if path:
                self.label.setText(path) 
                           
        self.button.clicked.connect(on_button_click)
        
        self.Cwidgets.add_Layout(self.button, self.main_layout)
        self.Cwidgets.add_Layout(self.label, self.main_layout)

        self.window.show()

    def get_file(self):
        path = self.Cwidgets.open_dialog(self.main_layout)

        if path:
            saveDict = {"mode": "file",
                        "path": path}
            save_to_json(saveDict, self.jsonTargetPath)


if __name__ == "__main__":
    app = App()
    sys.exit(app.Cwidgets.app.exec_())
