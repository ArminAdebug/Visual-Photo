import sys
from customWidgets import CustumWidgets
from file_manage.jsonManager import *


class App:
    def __init__(self):
        self.Cwidgets = CustumWidgets()
        self.window = self.Cwidgets.setupWindow()

        self.main_layout = self.Cwidgets.create_layout()

        self.window.setLayout(self.main_layout)

        self.jsonTargetPath = "..\data\TargetPath.json"

        self.label = self.Cwidgets.Label(
            "choice effect", self.window, (150, 350), 50)

        self.button = self.Cwidgets.create_button(self.window)
        self.button.clicked.connect(self.get_file)

        self.Cwidgets.add_Layout(self.button, self.main_layout)
        self.Cwidgets.add_Layout(self.label, self.main_layout)

        self.window.show()

    def get_file(self):
        path = self.Cwidgets.open_dialog(self.window, mode="directory")

        if path:
            self.label.setText(path)
            saveDict = {"mode": "file",
                        "path": path}
            save_to_json(saveDict, self.jsonTargetPath)


if __name__ == "__main__":
    app = App()
    sys.exit(app.Cwidgets.app.exec_())
