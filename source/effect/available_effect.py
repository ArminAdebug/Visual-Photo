from ..file_manage.jsonManager import load_from_json
import os
from pathlib import Path
import importlib.util

from photo_blur import blur
from photo_glow import glow
from photo_edge import edge
from photo_gray_scale import gray_scale
from photo_negate import negate
from photo_vintage import vintage

def _exists(path):
    exs = os.path.exists(path)
    return exs


def _open_access(path):
    access = os.access(path, os.X_OK)
    return access


def _get_mod_func(data):

    print(data)

    func_list = []
    for file, name in (data):
        try:
            print(file.stem)
            spec = importlib.util.spec_from_file_location(str(file), str(file))

            if spec is None:
                print(f"error: file <{file}> not find")

            try:
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                func_list.append(getattr(spec, name))

            except Exception:
                print("error unknown")
                continue

        except (ModuleNotFoundError, ImportError):
            # TODO: add error log: module not found, import error, function not found
            print("module not found")
            continue

    return func_list


info_path = Path(r"source\effect\effects_info.json").absolute()

effects_info = load_from_json(info_path)

effect_paths = [Path(path).absolute() for path in effects_info["paths"]]
effect_names = effects_info["effects"]

effects = list(zip(effect_paths, effect_names))

effects_filtered1 = [effect for effect in effects if _exists(effect[0])]
effects_filtered2 = [effect for effect in effects if _open_access(effect[0])]

effect_filter_listed = list(effects_filtered2)
print("effect_filter_listed", effect_filter_listed)
available_effects = []


if func_resault := _get_mod_func(effect_filter_listed):


    # TODO: ask memory manage vs style

    # available_effects The final result
    print(available_effects)

else:
    print("error imports")