import subprocess
from .effect.available_effect import available_effects
import ctypes

def basic_msgbox(text, title="error"):
    ctypes.windll.user32.MessageBoxW(0, text, title, 0x40 | 0x1)
    
class RunEffect:
    def __init__(self):
        self.Av_Ef = available_effects
        
    def run(self, effect_name):
        isAvailable = self._check_name(effect_name)

        if not isAvailable:
            # TODO: add error message
            print("effect is not available!")
            return 
        
        path = [effect[0] for effect in self.Av_Ef if effect[1] == effect_name][0]
        print(path)
        basic_msgbox(f"path:{path}", "check")
        
        subprocess.run(['python', path])
        
        try: 
            state_run = subprocess.run(
                ['python', r"C:\Users\Armin\Documents\Code\Python\Portfolio\photo editor\source\effect\photo_gray_scale.py"],
                capture_output=True,
                text=True
            )

            if state_run.returncode > 0:
                # TODO: add error message
                print("The effect did not run successfully.")

        except subprocess.CalledProcessError as e:
            print(f"error, masage: {e.stderr}")
            
            
        """ def __call__(self, effect_name):
        isAvailable = self._check_name(effect_name)

        if not isAvailable:
            # TODO: add error message
            print("effect is not available!")
            return 
        
        path = [effect[0] for effect in self.Av_Ef if effect[1] == effect_name][0]
        print(path)
        try: 
            state_run = subprocess.run(
                ['python', path],
                capture_output=True,
                text=True
            )

            if state_run.returncode > 0:
                # TODO: add error message
                print("The effect did not run successfully.")

        except subprocess.CalledProcessError as e:
            print(f"error, masage: {e.stderr}")
        """       
    def _check_name(self, name):
        if name.lower() in [effect[1] for effect in self.Av_Ef]:
            return True
        
        basic_msgbox("check name did not see a match", "error")
        
        return False
