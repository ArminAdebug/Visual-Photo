from source.display_manage import DisplayManage
from PyQt5.QtWidgets import QApplication
import sys
from pathlib import Path
import ctypes

# ctypes.windll.shell32.ShellExecuteW(
#    None, "runas", "python", str(Path(__file__).parent), None, 1)

{
    "last_file": "",
    "last_dir": ""
}

def main():
    app = QApplication(sys.argv)
    window = DisplayManage()
    
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()


# TODO: add errors on log during app runned
