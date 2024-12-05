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

    def get_data_item(name,type_return,data):
        for i in data.produtos:
            if i == name:
                return i[type_return]
            else:
                return