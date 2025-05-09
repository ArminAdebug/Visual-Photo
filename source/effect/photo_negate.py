from PIL import Image
from source.getImgpaths import get_directory_files
from source.jsonManager import *
from source.ToArray import Array_from_img_path

jsonTargetPath = "TargetPath.json"

json_data_dict = load_from_json(jsonTargetPath)

format_saving = ".png"
if json_data_dict["mode"] == "directory":
    
    for image in get_directory_files(json_data_dict["path"]):
        array =  Array_from_img_path(f"{json_data_dict["path"]}\\{image}")
        array = 255 - array
        
        savepath = str(f"{json_data_dict["path"]}\\{image[0: len(image) - 4]}Revers{format_saving}")
        imagesave = Image.fromarray(array).save(savepath)
        
        print("image", image[0:len(image) - 4], "saved!")
        
elif json_data_dict["mode"] == "file":
    image = json_data_dict["path"]
    array =  Array_from_img_path(image)
    array = 255 - array
    
    imagesave = Image.fromarray(array) 
    