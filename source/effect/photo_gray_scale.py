from PIL import Image
from ..file_manage.getImgpaths import get_directory_files
from ..file_manage.jsonManager import *


jsonTargetPath = "TargetPath.json"

json_data_dict = load_from_json(jsonTargetPath)

format_saving = ".png"
if json_data_dict["mode"] == "directory":

    for image in get_directory_files(json_data_dict["path"]):
        imagePIL = Image.open(
            json_data_dict["path"] + "\\" + image).convert("L")

        savepath = str(
            f"{json_data_dict["path"]}\\{image[0: len(image) - 4]}BlackWhite{format_saving}")
        imagePIL.save(savepath)

        print("image", image[0:len(image) - 4], "saved!")

elif json_data_dict["mode"] == "file":
    image = json_data_dict["path"]
    image1 = Image.open(image).convert("L")

    savepath = str(image[0: len(image) - 4] + f"BlackWhite{format_saving}")
    image1.save(savepath)
