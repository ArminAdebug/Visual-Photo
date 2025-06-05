from source.display_manage import DisplayManage
from PyQt5.QtWidgets import QApplication
import sys
from pathlib import Path
import ctypes

from source.data_forge import data_base_manage

# ctypes.windll.shell32.ShellExecuteW(
#    None, "runas", "python", str(Path(__file__).parent), None, 1)

# load error logs and tell problems


def warning():
    db_path = Path(r"data\data_bases\error_log.db").absolute()
    error_db = data_base_manage.DataBaseManager(db_path, {"table name":"errorlog", "subject":"errorlog"})
    
    error_db.write(*["unimportant file Not found", 6, 1])


def main():
    warning()
    app = QApplication(sys.argv)
    window = DisplayManage()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()


# TODO: add errors on log during app runned
