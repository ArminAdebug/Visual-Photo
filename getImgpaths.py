import os

available_types = (
        ".BMP", ".DIB", ".GIF", ".ICNS", ".ICO", ".IM", 
        ".JPEG", ".JPG", ".MSP", ".PCX", ".PNG", ".PPM", 
        ".PGM", ".PBM", ".SGI", ".SPIDER", ".TIFF", ".XBM",
    )


def get_directory_files(path):
    filepaths = list(os.listdir(path))
    filepaths = filter(lambda x:
        x[len(x)-4:len(x)] in available_types or
        x[len(x)-4:len(x)] in [word.lower() for word in available_types],
        filepaths)
    
    return filepaths
