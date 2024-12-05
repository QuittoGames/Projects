import os
import platform
from dataclasses import dataclass
from data import data


@dataclass
class tool:
    def clear_screen():
        if data.OS == "Windows":
            os.system('cls')
        else:
            os.system('clear')

    def verify_moudules():
        try:
            for i in data.modules:
                os.system(f"pip3 install {i}")
                tool.clear_screen()
        except Exception as E:
            print(f"Erro Na Intaçao De Modulos De Depencias!, Erro: {E}")
#Project created successfully!