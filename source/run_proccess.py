import subprocess
from .effect.available_effect import available_effects


class RunEffect:
    def __init__(self, effect):
        self.Av_Ef = available_effects

    def run(self, effect_name):
        isAvailable = self._check_name(effect_name)

        if not isAvailable:
            # TODO: add error message
            print("effect is not available!")
            return  
        
    def _check_name(self, name):
        if name in [effect[1] for effect in self.Av_Ef]:
            return True
        return False
