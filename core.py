from source.effect.photo_negate import negate
import source.display as display
# TODO: add errors on log
import ctypes
from pathlib import Path

ctypes.windll.shell32.ShellExecuteW(
    None, "runas", "python", str(Path(__file__).parent), None, 1)


negate()


def main():
    # window = display.Display()
    pass


if __name__ == "__main__":
    main()
