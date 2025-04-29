from PIL import Image
from getImgpaths import get_directory_files
from jsonManager import *


jsonTargetPath = "TargetPath.json"

json_data_dict = load_from_json(jsonTargetPath)

format_saving = ".png"
if json_data_dict["mode"] == "directory":
    
    for image in get_directory_files(json_data_dict["path"]):
        image1 = Image.open(image).convert("L")

        savepath = str(image[0: len(image) - 4] + f"BlackWhite{format_saving}")
        image1.save(savepath)
        
        print(image[0:len(image) - 4])
        
elif json_data_dict["mode"] == "file":
    image = json_data_dict["path"]
    image1 = Image.open(image).convert("L")

    savepath = str(image[0: len(image) - 4] + f"BlackWhite{format_saving}")
    image1.save(savepath)