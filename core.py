import source.display as display
# TODO: add errors on log
import ctypes
from pathlib import Path

ctypes.windll.shell32.ShellExecuteW(None, "runas", "python", str(Path(__file__).parent), None, 1)

def main():
    window = display.Display()


if __name__ == "__main__":
    main()
