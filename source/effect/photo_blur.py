from PIL import Image
from PIL import ImageFilter
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
            print("asd")
            imagePIL = imagePIL.filter(ImageFilter.BoxBlur(10))

            savepath = get_save_path(image, export_dict["copy"], "_blur")
            imagePIL.save(savepath)
            print("asd2")

    elif export_dict["mode"] == "file":
        image = target_path
        print("asd2")
        imagePIL = Image.open(image)
        imagePIL = imagePIL.filter(ImageFilter.BoxBlur(10))
        print("ge")
        savepath = get_save_path(image, export_dict["copy"], "_blur")
        print("ge2")
        imagePIL.save(savepath)
        print("afaster")
