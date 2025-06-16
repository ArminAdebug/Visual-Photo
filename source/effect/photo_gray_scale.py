from PIL import Image
from source.file_manage.getImgpaths import get_directory_files
from source.file_manage.jsonManager import *
from pathlib import Path


def main():
    target_path = Path(r"data\export_data\target_path.json").absolute()
    mode_path = Path(r"data\export_data\mode.json").absolute()

    target_path = load_from_json(target_path)["path"]
    export_dict = load_from_json(mode_path)
    
    if export_dict["mode"] == "directory":
        for image in get_directory_files(target_path):
            imagePIL = Image.open(image).convert("L")

            savepath = Path.joinpath(
                image.parent, image.stem + "_grayscale" + image.suffix)
            imagePIL.save(savepath)

            print("image", image.name, "saved!")

    elif export_dict["mode"] == "file":
        image = Path(target_path)
        image1 = Image.open(image).convert("L")

        savepath = Path.joinpath(
            image.parent, image.stem + "_grayscale" + image.suffix)
        image1.save(savepath)
