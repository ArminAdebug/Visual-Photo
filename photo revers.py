from PIL import Image
from getImgpaths import get_directory_files
from ToArray import make_Array_from_image

format_saving = ".png"
for image in get_directory_files(r"."):
    array =  make_Array_from_image(image)
    array = 255 - array
    
    imagesave = Image.fromarray(array) 
    
    print(imagesave, "s")
    
    savepath = str(image[0: len(image) - 4] + f"BlackWhite{format_saving}")
    imagesave.save(savepath)
    
    print(image[0:len(image) - 4])
