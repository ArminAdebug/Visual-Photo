from source.effect.photo_vintage import thermal
import source.display as display
# TODO: add errors on log during app runned
import ctypes

#ctypes.windll.shell32.ShellExecuteW(
#    None, "runas", "python", str(Path(__file__).parent), None, 1)


thermal()


def main():
    # window = display.Display()
    pass


if __name__ == "__main__":
    main()
