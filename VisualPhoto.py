import subprocess
import os
import ctypes
from pathlib import Path

def basic_msgbox(text, title):
    ctypes.windll.user32.MessageBoxW(0, text, title, 0x40 | 0x1)


def check_core(path):
    if not os.path.exists(path):
        print("1")  # TODO: insert with real masage box

        return False

    elif not os.access(path, os.X_OK):
        print("2")
        return False

    return True


core_path = Path(r"core.py").absolute()

if __name__ == "__main__":
    state_check = check_core(core_path)

    if state_check:
        try:
            state_run = subprocess.run(
                ['python', core_path],
                capture_output=True,
                text=True
            )

            if state_run.returncode > 0:
                basic_msgbox(
                    "core.py Encountered an execution failure.", "Error")

        except subprocess.CalledProcessError as e:
            print(f"error, masage: {e.stderr}")
