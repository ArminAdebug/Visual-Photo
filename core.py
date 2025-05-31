import source.display as display
# TODO: add errors on log
import ctypes
from pathlib import Path

ctypes.windll.shell32.ShellExecuteW(None, "runas", "python", str(Path(__file__).parent), None, 1)

from source.effect.photo_blur import blur

blur()

def main():
    #window = display.Display()
    pass

if __name__ == "__main__":
    main()
