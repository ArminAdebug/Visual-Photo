from PIL import Image, ImageFilter
from source.file_manage.getImgpaths import get_directory_files
from source.file_manage.jsonManager import *
from pathlib import Path
import cv2

def main():
    target_path = Path(r"data\export_data\target_path.json").absolute()
    mode_path = Path(r"data\export_data\mode.json").absolute()

    target_path = "F:\\docc\\armin\\+GAME'S\\Dev\\Code\\Python\\Portfolio\\image test folder" #load_from_json(target_path)["path"]
    export_dict = load_from_json(mode_path)
    
    if export_dict["mode"] == "directory":
        for image in get_directory_files(target_path):
            savepath = Path.joinpath(
                image.parent, image.stem + "_oil" + image.suffix)
            
            img = cv2.imread(image)
            res = cv2.xphoto.oilPainting(img, 5, 10)
            cv2.imwrite(savepath, res)
            
            print("image", image.name, "saved!")

    elif export_dict["mode"] == "file":
        image = Path(target_path)
        savepath = Path.joinpath(
            image.parent, image.stem + "_oil" + image.suffix)
        
        img = cv2.imread(image)
        res = cv2.xphoto.oilPainting(img, 5, 10)
        cv2.imwrite(savepath, res)
        
        print("image", image.name, "saved!")
