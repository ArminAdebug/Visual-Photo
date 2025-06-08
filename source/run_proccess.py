#from .effect.available_effect import available_effects
import ctypes

from .effect.photo_blur import blur
from .effect.photo_glow import glow
from .effect.photo_mosaic import mosaic
from .effect.photo_gray_scale import gray_scale
from .effect.photo_negate import negate
from .effect.photo_vintage import vintage


def basic_msgbox(text, title="error"):
    ctypes.windll.user32.MessageBoxW(0, text, title, 0x40 | 0x1)


class RunEffect:
    def __call__(self, effect_name):
        match effect_name:
            case "gray_scale":
                gray_scale()
            case "negate":
                negate()
            case "blur":
                blur()
            case "glow":
                glow()
            case "mosaic":
                mosaic()
            case "vintage":
                vintage()
            case "oil":
                pass
            case _:
                basic_msgbox("effect name unavailable.")
