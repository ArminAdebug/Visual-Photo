from PIL import Image, ImageFilter
from ..file_manage.getImgpaths import get_directory_files
from ..file_manage.jsonManager import *
from pathlib import Path


def oil():
    jsonTargetPath = Path(r"data\TargetPath.json").absolute()

    json_data_dict = load_from_json(jsonTargetPath)

    if json_data_dict["mode"] == "directory":
        for image in get_directory_files(json_data_dict["path"]):
            imagePIL = Image.open(image)
            
            smoothed = imagePIL.filter(ImageFilter.SMOOTH_MORE)
    
            gray = smoothed.convert('L')

            edges = gray.filter(ImageFilter.FIND_EDGES)

            edges = edges.point(lambda x: 255 if x > 50 else 0)
            edges = edges.point(lambda x: 255 if x > 50 else 0)


            small = smoothed.resize((smoothed.width // 4, smoothed.height // 4), 
                                resample=Image.BILINEAR)
            quantized = small.resize(smoothed.size, Image.NEAREST)
            


            mask = edges.convert('1')

            cartoon = Image.composite(quantized, Image.new('RGB', imagePIL.size, 'black'), mask)
            
            savepath = Path.joinpath(
                image.parent, image.stem + "_oil" + image.suffix)

            cartoon.save(savepath)

            print("image", image.name, "saved!")

    elif json_data_dict["mode"] == "file":
        image = Path(json_data_dict["path"])

        imagePIL = Image.open(image)
        imagePIL = imagePIL.point(lambda p: 255 - p)

        savepath = Path.joinpath(
            image.parent, image.stem + "_oil" + image.suffix)

        imagePIL.save(savepath)
