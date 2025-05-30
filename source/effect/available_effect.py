from ..file_manage.jsonManager import load_from_json
import os
from pathlib import Path
import importlib.util


def _get_effects_info(info_path):
    data_dict = load_from_json(info_path)
    return data_dict


def _exists(path):
    exs = os.path.exists(path)
    return exs


def _open_access(path):
    access = os.access(path, os.X_OK)
    return access


def _get_mod_func(paths):

    print(paths)

    func_list = []
    for file in (paths):
        try:
            print(file.stem)
            spec = importlib.util.spec_from_file_location(file, str(file))

            if spec is None:
                print(f"error: file <{file}> not find")

            try:
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                func_list.append(spec.main)

            except Exception as e:
                continue

        except (ModuleNotFoundError, ImportError):
            # TODO: add error log: module not found, import error, function not found
            continue

    return func_list


info_path = Path(r"source\effect\effects_info.json").absolute()

effects_info = _get_effects_info(info_path)

effect_paths = [Path(path).absolute() for path in effects_info["paths"]]
effect_names = effects_info["effects"]

effects = list(zip(effect_paths, effect_names))

effects_filtered1 = [effect for effect in effects if _exists(effect[0])]
effects_filtered2 = [effect for effect in effects if _open_access(effect[0])]

effect_filter_listed = list(effects_filtered2)

available_effects = []
#print("1", effect_filter_listed)
#print("2", map(lambda effect_tuple: effect_tuple, effect_filter_listed))
#print("3", map(lambda effect_tuple: effect_tuple[0], effect_filter_listed))
#print("4", list(map(lambda effect_tuple: effect_tuple[0], effect_filter_listed)))
#
if _get_mod_func(list(map(lambda effect_tuple: effect_tuple[0], effect_filter_listed))) != None:
    available_effects = list(map(
        lambda effect_tuple: (_get_mod_func(list(map(
            lambda effect_tuple: effect_tuple[0], effect_filter_listed))),
            effect_tuple[1]),
        effect_filter_listed
    )
    )

# TODO: ask memory manage vs style

 # available_effects The final result
print(available_effects)
