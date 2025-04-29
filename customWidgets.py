import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QWidget, QGridLayout, QPushButton, QLabel, QComboBox, QSpinBox, QDoubleSpinBox, QCheckBox, QLineEdit, QFileDialog
from PyQt5.QtGui import QFont, QFontDatabase
from PyQt5.QtCore import QObject
from FontPaths import *


class CustumWidgets(QObject):
    def __init__(self):
        super().__init__()

        self.app = QApplication(sys.argv)
        self.defaultFont = self.get_font(defaultFontPath)
        self.BoldFont = self.get_font(boldFontPath)
        self.warningFont = self.get_font(warningFontPath)
        self.ClassicFont = self.get_font(classicFontPath)

        self.default_layout = self.create_layout()

    def setupWindow(self, background=""):
        self.window = QWidget()
        self.window.setGeometry(0, 0, 1920, 1080)
        self.window.setMinimumSize(384, 216)
        return self.window

    def create_layout(
        self, layout_type="vbox", spacing=10, margins=(10, 10, 10, 10)
    ):
        if layout_type == "vbox":
            layout = QVBoxLayout()
        elif layout_type == "hbox":
            layout = QHBoxLayout()
        elif layout_type == "grid":
            layout = QGridLayout()

        layout.setSpacing(spacing)
        layout.setContentsMargins(*margins)  # (left, top, right, bottom)
        return layout

    def add_Layout(self, widget, layout=None):
        if layout == None:
            self.default_layout.addWidget(widget)
        else:
            layout.addWidget(widget)

    def get_font(self, font_path, font_size=12):
        try:
            font_id = QFontDatabase.addApplicationFont(font_path)
            if font_id == -1:
                print(f"Font not found: {font_path}")
                return QFont("Arial", font_size)

            font_families = QFontDatabase.applicationFontFamilies(font_id)
            if not font_families:
                # TODO: add error handling
                print("No font families found in the font file")
                return QFont("Arial", font_size)

            font_family = font_families[0]
            return QFont(font_family, font_size)

        except Exception as e:
            print(f"Error loading font: {e}, using fallback font.")
            return QFont("Arial", font_size)

    def Label(self, text, parent, pos, size=20, colorcode="#fefff", stylemode="default", Layout=None):
        self.label = QLabel(text, parent)
        self.label.setGeometry(0, 0, 200, 100)

        styleCodeKey = {
            "color": f"color: {colorcode};",
            "sizecode": f" font-size: {size}px;"
        }

        if stylemode == "default":
            self.label.setStyleSheet(
                "\n {color} {sizecode}\n ".format(**styleCodeKey)
            )
            self.label.setFont(self.defaultFont)

        return self.label

    def input(self, parent, input_type="text", placeholder="", style="default", Layout=None):
        self.input_widget = QLineEdit(parent)
        self.input_widget.setPlaceholderText(placeholder)

        self.input_widget.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                border: 1px solid #3498db;
                border-radius: 4px;
                font-size: 14px;
            }
        """)

        if not Layout:
            self.input_widget.add_Layout(Layout)
        else:
            self.input_widget.add_Layout(self.default_layout)

        return self.input_widget

    def create_button(self, parent, text="Button", style="default", icon=None):
        button = QPushButton(text, parent)

        # استایل پیشفرض
        if style == "default":
            button.setStyleSheet("""
                QPushButton {
                    background: #3498db;
                    color: white;
                    padding: 10px 20px;
                    border-radius: 5px;
                }
                QPushButton:hover { background: #2980b9; }
            """)
        # آیکون (اختیاری)
        if icon:
            button.setIcon(QIcon(icon))

        return button

    def open_dialog(self, parent, title="select file", mode="file"):
        step = 0
        print(f"open dialog {step}")
        step += 1
        dialog = QFileDialog(parent)
        print(f"open dialog {step}")
        step += 1
        dialog.setWindowTitle(title)
        print(f"open dialog {step}")
        step += 1
        if mode == "file":
            print(f"open dialog {step}")
            step += 1
            dialog.setFileMode(QFileDialog.ExistingFile)
        elif mode == "directory":

            print(f"open dialog {step}")
            step += 1
            dialog.setFileMode(QFileDialog.Directory)
        if dialog.exec_():

            print(f"open dialog {step}")
            step += 1
            return dialog.selectedFiles()[0]
        return ""

# button and input folder
