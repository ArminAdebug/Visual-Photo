#from .effect.available_effect import available_effects
import ctypes
from .effect.photo_gray_scale import main

def basic_msgbox(text, title="error"):
    ctypes.windll.user32.MessageBoxW(0, text, title, 0x40 | 0x1)
    
class RunEffect:
    def __init__(self):
        pass
        
    def run(self, effect_name):
        main()

