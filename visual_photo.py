from source.display_manage import DisplayManage
from PyQt5.QtWidgets import QApplication
import sys

from source.handling_errors import log_error

from source.tool.massage_box import MassageBox


def preflight_checks(e_manager: log_error.ErrorManager):
    """checks app errors and health at startup"""
    error_list = e_manager.shows()

    e_manager.log(5)

    print("startup check errors:", error_list)


def main():
    app = QApplication(sys.argv)
 
    #TODO: complite error_log and show error for user
    e_manager = log_error.ErrorManager(__file__)

    preflight_checks(e_manager)

    try:
        window = DisplayManage()

        state = app.exec_()
        e_manager.finish()
        sys.exit(state)

    finally:
        e_manager.finish()
        print("program crashs unexpectedly.")
        sys.exit(1)


if __name__ == "__main__":
    main()
