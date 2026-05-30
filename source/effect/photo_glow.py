from PIL import Image, ImageFilter, ImageChops
from source.file_manage.getImgpaths import get_directory_files
from source.file_manage.jsonManager import *
from pathlib import Path

from source.effect.common import get_save_path


def main():
    target_path_config = Path(r"data\export_data\target_path.json").absolute()
    mode_path = Path(r"data\export_data\mode.json").absolute()

    target_path = Path(load_from_json(target_path_config)["path"]).absolute()
    export_dict = load_from_json(mode_path)

    if export_dict["mode"] == "directory":
        for image in get_directory_files(target_path):
            imagePIL = Image.open(image)

            blur = imagePIL.filter(ImageFilter.GaussianBlur(5))
            imagePIL = ImageChops.add(imagePIL, blur)

            savepath = get_save_path(image, export_dict["copy"], "_glow")

            imagePIL.save(savepath)

    elif export_dict["mode"] == "file":
        image = Path(target_path)

        imagePIL = Image.open(image)

        blur = imagePIL.filter(ImageFilter.GaussianBlur(5))
        imagePIL = ImageChops.add(imagePIL, blur)

        savepath = get_save_path(image, export_dict["copy"], "_glow")
        imagePIL.save(savepath)
