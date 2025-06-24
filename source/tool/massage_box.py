from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QGridLayout, QLabel, QSystemTrayIcon
from .massage_box_ui import Ui_Dialog

class MassageBox:
    def __init__(self, data, title, parent=None, mode=("massage", "info")):
        super().__init__()

        self.is_app_availabe = QApplication.instance()

        if not self.is_app_availabe:
            self.pop_up_window_app = QApplication([])

        if mode[0] == "massage":
            if mode[1] == "warning":
                self.massage_box = QMessageBox.warning(parent, title, data)
            
            elif mode[1] in ("info", "information"):
                self.massage_box = QMessageBox.information(parent, title, data)
            
            elif mode[1] == "critical":
                self.massage_box = QMessageBox.critical(parent, title, data)
            
            else :
                raise ValueError

            #self.massage_box_layout = QGridLayout()
            #self.massage_lable = QLabel(data)
            #
            #self.massage_box_layout.addWidget(self.massage_lable)
            #self.massage_box.setLayout(self.massage_box_layout)
            #
            #self.massage_box.show()
        
        elif mode[0] == "list":
            self.pop_up_window = QDialog(None)

            self.ui = Ui_Dialog()
            self.ui.setupUi(self.pop_up_window)

            self.pop_up_window.show()
            
        if self.is_app_availabe and parent:
            self.pop_up_window_app.exec_()

