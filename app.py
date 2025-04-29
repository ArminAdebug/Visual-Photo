import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QInputDialog
import time
from customWidgets import CustumWidgets


Cwidgets = CustumWidgets()
window = Cwidgets.setupWindow()

main_layout = Cwidgets.create_layout()

window.setLayout(main_layout)

label = Cwidgets.Label("helloo test Cwidgets", window, (50, 50), 50)
Cwidgets.add_Layout(label, main_layout)
window.show()
sys.exit(Cwidgets.app.exec_())
