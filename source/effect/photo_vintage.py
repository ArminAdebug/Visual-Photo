from PIL import Image
from source.file_manage.getImgpaths import get_directory_files
from source.file_manage.jsonManager import *
from pathlib import Path
import random

from source.effect.common import get_save_path


def main():
    target_path_config = Path(r"data\export_data\target_path.json").absolute()
    mode_path = Path(r"data\export_data\mode.json").absolute()

    target_path = Path(load_from_json(target_path_config)["path"])
    export_dict = load_from_json(mode_path)

    if export_dict["mode"] == "directory":
        for image in get_directory_files(target_path):

            imagePIL = Image.open(image)

            pixels = imagePIL.load()

            for x in range(imagePIL.width):
                for y in range(imagePIL.height):
                    rand = random.randint(1, 21)
                    if rand == 1 or rand == 2:
                        pixels[x, y] = (0, 0, 0)

                    elif rand == 3:
                        pixels[x, y] = (255, 255, 255)

                    else:
                        r, g, b = pixels[x, y]
                        intensity = sum((r, g, b)) // 3

                        pixels[x, y] = (intensity, round(intensity * 0.5), 0)

            savepath = get_save_path(image, export_dict["copy"], "_vintage")
            imagePIL.save(savepath)

    elif export_dict["mode"] == "file":
        image = Path(target_path)

        imagePIL = Image.open(image)

        pixels = imagePIL.load()

        for x in range(imagePIL.width):
            for y in range(imagePIL.height):
                rand = random.randint(1, 30)
                if rand == 1 or rand == 2:
                    pixels[x, y] = (0, 0, 0)

                elif rand == 3:
                    pixels[x, y] = (255, 255, 255)

                else:
                    r, g, b = pixels[x, y]
                    intensity = sum((r, g, b)) // 3

                    pixels[x, y] = (intensity, round(intensity * 0.5), 0)

        savepath = get_save_path(image, export_dict["copy"], "_vintage")
        imagePIL.save(savepath)
