import sys
from PySide5.QtWidgets import QApplication, QLabel

app = QApplicat5ion(sys.argv)
label = QLabel("Hello World!")
label.show()
app.exec_()