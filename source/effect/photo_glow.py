from PIL import Image, ImageFilter, ImageChops
from ..file_manage.getImgpaths import get_directory_files
from ..file_manage.jsonManager import *
from pathlib import Path


def glow():
    jsonTargetPath = Path(r"data\TargetPath.json").absolute()

    json_data_dict = load_from_json(jsonTargetPath)

    if json_data_dict["mode"] == "directory":
        for image in get_directory_files(json_data_dict["path"]):
            imagePIL = Image.open(image)
            
            blur = imagePIL.filter(ImageFilter.GaussianBlur(5))
            imagePIL = ImageChops.add(imagePIL, blur)
            
            savepath = Path.joinpath(image.parent, image.stem + "_glow" + image.suffix)
            
            imagePIL.save(savepath)

            print("image", image.name, "saved!")

    elif json_data_dict["mode"] == "file":
        image = Path(json_data_dict["path"])
        
        imagePIL = Image.open(image)
    
        blur = imagePIL.filter(ImageFilter.GaussianBlur(5))
        imagePIL = ImageChops.add(imagePIL, blur)
        

        savepath = Path.joinpath(image.parent, image.stem + "_glow" + image.suffix)
        imagePIL.save(savepath)
