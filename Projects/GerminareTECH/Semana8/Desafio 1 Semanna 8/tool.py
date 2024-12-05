import os
import platform
from dataclasses import dataclass

@dataclass  
class tool:
    def clear_screen():
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')

    juros = lambda c,i,t: c(1+i)**t
