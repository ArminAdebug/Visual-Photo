import numpy as np
import PIL.Image as Image

def make_Array_from_image(ImgName):
    try :
        img = Image.open(ImgName)

        array = np.array(img)
    except BaseException:
        array = np.zeros((0,0,3))
    return array

