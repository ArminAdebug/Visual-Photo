from PIL import Image, ImageFilter, ImageChops
from source.file_manage.getImgpaths import get_directory_files
from source.file_manage.jsonManager import *
from pathlib import Path


def _save_path(path: Path, copy: bool):
    if copy:
        savepath = Path.joinpath(
            path.parent, path.stem + "_blur" + path.suffix)
        return savepath
    return path


def main():
    target_path = Path(r"data\export_data\target_path.json").absolute()
    mode_path = Path(r"data\export_data\mode.json").absolute()

    target_path = load_from_json(target_path)["path"]
    export_dict = load_from_json(mode_path)

    if export_dict["mode"] == "directory":
        for image in get_directory_files(target_path):
            imagePIL = Image.open(image)

            blur = imagePIL.filter(ImageFilter.GaussianBlur(5))
            imagePIL = ImageChops.add(imagePIL, blur)

            savepath = _save_path(image, export_dict["copy"])

            imagePIL.save(savepath)

            print("image", image.name, "saved!")

    elif export_dict["mode"] == "file":
        image = Path(target_path)

        imagePIL = Image.open(image)

        blur = imagePIL.filter(ImageFilter.GaussianBlur(5))
        imagePIL = ImageChops.add(imagePIL, blur)

        savepath = _save_path(image, export_dict["copy"])
        imagePIL.save(savepath)
