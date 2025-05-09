import os
import os

current_dir = os.path.dirname(__file__)

def _get_font_path(path):
    file_path = os.path.join(current_dir, "..", "..", path)
    file_path = os.path.abspath(file_path)
    return file_path


defaultFontPath= _get_font_path(r"asset\fonts\Special_Gothic_Condensed_One\SpecialGothicCondensedOne-Regular.ttf")
boldFontPath= _get_font_path(r"..\..\asset\fonts\Special_Gothic_Expanded_One\SpecialGothicExpandedOne-Regular.ttf")
warningFontPath = _get_font_path(r"..\..\asset/fonts/Roboto_Mono/RobotoMono-Italic-VariableFont_wght.ttf")
classicFontPath = _get_font_path(r"..\..\asset\fonts\Playwrite_RO\PlaywriteRO-VariableFont_wght.ttf")
