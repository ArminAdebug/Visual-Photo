from source.file_manage.jsonManager import load_from_json
import os
from pathlib import Path
import importlib.util


def _exists(path):
    exs = os.path.exists(path)
    return exs


def _run_access(path):
    access = os.access(path, os.X_OK)
    return access


def _get_mod_func(data):
    
    func_list = []
    for file in (data):
        try:
            spec = importlib.util.spec_from_file_location(str(file), str(file))

            if spec is None:
                print(f"error: file <{file}> not find")

            try:
                module = importlib.util.module_from_spec(spec)

                spec.loader.exec_module(module)
                func_list.append(getattr(module, "main"))

            except Exception as e:
                print(e)
                continue

        except (ModuleNotFoundError, ImportError):
            # TODO: add error log: module not found, import error, function not found
            print("module not found")
            continue

    return func_list


info_path = Path(r"source\effect\effects_info.json").absolute()

effects_info = load_from_json(info_path)

effect_paths = [Path(path).absolute() for path in effects_info["paths"]]

valid_paths = [e for e in effect_paths if _exists(e) and _run_access(e)]

available_effects = []

if func_resault := _get_mod_func(list(valid_paths)):

    # available_effects The final result
    available_effects = list(zip(effects_info["effects"], func_resault))

else:
    print("no effect loaded")
    # TODO: log error
