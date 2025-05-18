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

effect_paths = [Path(path).absolute() for path in effects_info["paths"]]
effect_names = effects_info["effects"]

effects = list(zip(effect_paths, effect_names))

effects_filtered1 = [effect for effect in effects if _exists(effect[0])]
effects_filtered2 = [effect for effect in effects if _open_access(effect[0])]

# TODO: ask memory manage vs style

available_effects = list(effects_filtered2)  # The final result
