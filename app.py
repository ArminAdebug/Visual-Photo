import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QInputDialog
import time

app = QApplication(sys.argv)
window = QWidget()
window.setGeometry(0, 0, 1920, 1080)
window.setMinimumSize(384, 216)
# font = QWidgent.font() # type: ignore

label = QLabel("Hello PyQt5!", window)
label.setStyleSheet("""
    QLabel {
        color: #ffff;
        font-size: 50px;
        font-family: Child Hood;
    }
""")


def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Start time
        result = func(*args, **kwargs)  # Call the original function
        end_time = time.time()  # End time
        label.setText(f"{end_time - start_time:.4f}")

        print(
            f"Function '{func.__name__}' executed in {end_time - start_time:.4f} seconds")

        return result
    return wrapper


@timer_decorator
def example_function(n1, n2):
    """A simple function that sums numbers from 1 to n."""
    resualt = n1 ** n2
    return resualt


window.show()

input1 = QInputDialog.getText(window, "Input", "number 1:")[0]

input2 = QInputDialog.getText(window, "Input", "number 2:")[0]

sys.exit(app.exec_())
