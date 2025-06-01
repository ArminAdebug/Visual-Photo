from PIL import Image
from ..file_manage.getImgpaths import get_directory_files
from ..file_manage.jsonManager import *
from pathlib import Path

import random


def vintage():
    jsonTargetPath = Path(r"data\TargetPath.json").absolute()

    json_data_dict = load_from_json(jsonTargetPath)

    if json_data_dict["mode"] == "directory":
        for image in get_directory_files(json_data_dict["path"]):
            
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

            savepath = Path.joinpath(
                image.parent, image.stem + "_vintage" + image.suffix)
            imagePIL.save(savepath)

            print("image", image.name, "saved!")

    elif json_data_dict["mode"] == "file":
        image = Path(json_data_dict["path"])

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

        savepath = Path.joinpath(
            image.parent, image.stem + "_vintage" + image.suffix)
        imagePIL.save(savepath)
