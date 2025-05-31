import os
from pathlib import Path

available_types = (
    '.bmp', '.dib', '.gif', '.icns', '.ico',
    '.im', '.jpeg', '.jpg', '.msp', '.pcx',
    '.png', '.ppm', '.pgm', '.pbm', '.sgi',
    '.spider', '.tiff', '.xbm'
)

def get_directory_files(path):
    
    filepaths = [Path("/".join((path, i))).absolute() for i in os.listdir(path)]
    #print([h for h in filepaths])
    #filepaths = list(filter(lambda x: x.is_file(), filepaths))

    filepaths = list(filter(lambda path:
        path.suffix.lower() in available_types,
        filepaths))

    return filepaths

a = get_directory_files(r"C:/Users/Armin/Documents/Code/Python/Portfolio/image test folder")
print("_______")
print(a)