from source.display_manage import DisplayManage
from PyQt5.QtWidgets import QApplication
import sys
from pathlib import Path
import ctypes


from source.handling_error import log_error 

# ctypes.windll.shell32.ShellExecuteW(
#    None, "runas", "python", str(Path(__file__).parent), None, 1)


# show filtered error during week
def preflight_checks(manager : log_error.ErrorManager):
    error_list = manager.shows()

    manager.log(6)
    
    print(error_list)

def main():
    e_manager = log_error.ErrorManager(__file__)
    
    preflight_checks(e_manager)
    
    app = QApplication(sys.argv)
    
    try:
        window = DisplayManage()
    
        if app.exec_() == 0:
            e_manager.finish()
            sys.exit()
        
    except Exception as e:
        print(e)
        
    finally:
        e_manager.finish()


if __name__ == "__main__":
    main()


# TODO: add errors on log during app runned
