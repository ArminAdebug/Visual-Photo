from .effect.available_effect import available_effects
import ctypes
from .file_manage.jsonManager import *
from pathlib import Path

effect_info_path = Path(r"source\effect\effects_info.json").absolute()
effect_names = load_from_json(effect_info_path)["effects"]

def basic_msgbox(text, title="error"):
    ctypes.windll.user32.MessageBoxW(0, text, title, 0x40 | 0x1)


class RunEffect:
    def __call__(self, effect_name):
        if not effect_name:
            # TODO: log error: 4 null effect selected
            pass
        elif effect_name not in effect_names:
            # TODO: log error: 7 unknown error selected
            pass
        elif effect_name not in [AE[0] for AE in available_effects]:
            # TODO: log error: 12 effect not available
            pass
        else:
            desired_func = [AE[1] for AE in available_effects if AE[0] == effect_name][0]
            
            desired_func()
