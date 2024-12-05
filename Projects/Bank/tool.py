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
    
    def verify_user(name):
        for i in data.users:
            if i.name == name:
                return True
        return
#Project created successfully!