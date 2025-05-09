import numpy as np
import PIL.Image as Image

def Array_from_img_path(ImgName):
    print(ImgName)
    try :
        img = Image.open(ImgName)
        array = np.array(img)
    except BaseException:
        array = np.zeros((0,0,3))
    return array

