from source.display_manage import DisplayManage
from PyQt5.QtWidgets import QApplication
import sys

#import ctypes
#ctypes.windll.shell32.ShellExecuteW(
#    None, "runas", "python", str(Path(__file__).parent), None, 1)

from source.handling_error import log_error

from source.tool.massage_box import MassageBox

def introduc():
    MassageBox("""سلام من آرمین اصغری هستم از مدرسه شهید صیاد شیرازی.
               من 15 سالمه و این برنامه روی عکس(ها) اثر های مختلفی از جمله تار شدن , سیاه و سفید و ... میزاره.
               با توچه به محدودیت زمان بیشترین تلاشم رو گزاشتم.""", "معرفی")

# show filtered error during week
def preflight_checks(e_manager: log_error.ErrorManager):
    error_list = e_manager.shows()

    e_manager.log(5)

    print(error_list)


def main():
    app = QApplication(sys.argv)
    
    introduc()
    
    e_manager = log_error.ErrorManager(__file__)

    preflight_checks(e_manager)

    try:
        window = DisplayManage()

        if app.exec_() == 0:
            e_manager.finish()
            

    except Exception as e:
        print(e)

    finally:
        e_manager.finish()
        sys.exit(0)


if __name__ == "__main__":
    main()

#TODO: complite error_log and show error for user