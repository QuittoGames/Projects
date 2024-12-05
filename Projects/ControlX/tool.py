import os
import platform
from dataclasses import dataclass
from data import data
import asyncio

@dataclass
class tool:
    def clear_screen():
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')
    
    async def verfy_modules():
        for i in data.modules:
            os.system(f"pip3 install {i}")
        
    def get_devices():
        pass
    async def wait_animetion(Function_await):
        mesage = ""
        while await Function_await:
            mesage + "."
            if len(mesage) == 2:mesage = str()
            print(f"Processando{mesage}", end="\r") 
        return 
    #Project created successfully!