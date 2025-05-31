from PIL import Image
from PIL import ImageFilter

from ..file_manage.getImgpaths import get_directory_files
from ..file_manage.jsonManager import *
from pathlib import Path


def blur():
    jsonTargetPath = Path(r"data\TargetPath.json").absolute()

    json_data_dict = load_from_json(jsonTargetPath)

    if json_data_dict["mode"] == "directory":
        print("debug")
        for image in get_directory_files(json_data_dict["path"]):
            imagePIL = Image.open(image)

            imagePIL = imagePIL.filter(ImageFilter.BoxBlur(10))

            savepath = Path.joinpath(
                image.parent, image.stem + "blur" + image.suffix)
            imagePIL.save(savepath)

            print("image", image.name, "saved!")

    elif json_data_dict["mode"] == "file":
        image = json_data_dict["path"]
        imagePIL = Image.open(image)
        imagePIL = imagePIL.filter(ImageFilter.BoxBlur(10))

        savepath = Path.joinpath(
            image.parent, image.stem + "blur" + image.suffix)

        imagePIL.save(savepath)
