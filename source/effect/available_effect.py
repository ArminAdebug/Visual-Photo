from ..file_manage.jsonManager import *
import os


"""
_current_dir = os.path.dirname(__file__)
def _get_font_path(path):
    file_path = os.path.join(_current_dir, "..", path)
    file_path = os.path.abspath(file_path)
    return file_path
"""


info_path = r".\effect_info.json"

def get_effects_info(info_path : str) -> dict:
    data_dict = load_from_json(info_path)
    return data_dict

def _exists(path):
    exs = os.path.exists(path)
    return exs


def _open_access(path):
    access = os.access(path, os.X_OK)
    return access



# print(_open_access("photo_gray_scale.py"))
