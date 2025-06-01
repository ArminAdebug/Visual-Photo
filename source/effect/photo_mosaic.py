from PIL import Image
from ..file_manage.getImgpaths import get_directory_files
from ..file_manage.jsonManager import *
from pathlib import Path


def mosaic():
    jsonTargetPath = Path(r"data\TargetPath.json").absolute()

    json_data_dict = load_from_json(jsonTargetPath)

    if json_data_dict["mode"] == "directory":
        for image in get_directory_files(json_data_dict["path"]):
            imagePIL = Image.open(image)

            small = imagePIL.resize(
                (imagePIL.width//10, imagePIL.height//10), resample=Image.NEAREST)
            imagePIL = small.resize(imagePIL.size, Image.NEAREST)

            savepath = Path.joinpath(
                image.parent, image.stem + "_mosaic" + image.suffix)
            imagePIL.save(savepath)

            print("image", image.name, "saved!")

    elif json_data_dict["mode"] == "file":
        image = Path(json_data_dict["path"])

        imagePIL = Image.open(image)

        small = imagePIL.resize(
            (imagePIL.width//10, imagePIL.height//10), resample=Image.NEAREST)
        imagePIL = small.resize(imagePIL.size, Image.NEAREST)

        savepath = Path.joinpath(
            image.parent, image.stem + "_mosaic" + image.suffix)
        imagePIL.save(savepath)
