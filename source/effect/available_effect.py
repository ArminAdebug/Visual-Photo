from ..file_manage.jsonManager import load_from_json
import os
from pathlib import Path


def _get_effects_info(info_path):
    data_dict = load_from_json(info_path)
    return data_dict


def _exists(path):
    exs = os.path.exists(path)
    return exs


def _open_access(path):
    access = os.access(path, os.X_OK)
    return access


info_path = Path(r"source\effect\effects_info.json").absolute()

effects_info = _get_effects_info(info_path)
effects_list = effects_info["paths"]

effects_filtered1 = filter(_exists, effects_list)

effects_filtered2 = filter(_open_access, list(effects_filtered1))

available_effect = list(effects_filtered2).copy()

print(available_effect)
