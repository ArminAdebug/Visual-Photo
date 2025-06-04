from PIL import Image
from ..file_manage.getImgpaths import get_directory_files
from ..file_manage.jsonManager import *
from pathlib import Path


def vintage():
    jsonTargetPath = Path(r"data\TargetPath.json").absolute()

    json_data_dict = load_from_json(jsonTargetPath)

    if json_data_dict["mode"] == "directory":
        for image in get_directory_files(json_data_dict["path"]):
            imagePIL = Image.open(image).convert("L")

            savepath = Path.joinpath(
                image.parent, image.stem + "_vintage" + image.suffix)
            imagePIL.save(savepath)

            print("image", image.name, "saved!")

    elif json_data_dict["mode"] == "file":
        image = Path(json_data_dict["path"])
        image1 = Image.open(image).convert("L")

        savepath = Path.joinpath(image.parent, image.stem + "_vintage" + image.suffix)
        image1.save(savepath)
