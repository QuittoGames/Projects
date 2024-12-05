import os
import platform
from dataclasses import dataclass
from data import data


@dataclass
class tool:
    def clear_screen():
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')
    
    media_notas = lambda x,y: x + y/2

    def verify_aproved(media):
        if media >= 7:
            return True
        else:
            return False