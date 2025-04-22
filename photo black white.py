from PIL import Image
from getpaths import get_files

format_saving = ".png"
for image in get_files(r"."):
    image1 = Image.open(image).convert("L")

    savepath = str(image[0: len(image) - 4] + f"BlackWhite{format_saving}")
    image1.save(savepath)
    
    print(image[0:len(image) - 4])
