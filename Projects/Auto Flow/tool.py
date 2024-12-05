import os
import platform
from dataclasses import dataclass
from data import data
from command import comamnds
from googlesearch import search
from time import sleep
from PyQt6.QtCore import QPropertyAnimation, QEasingCurve,QTimer


@dataclass
class tool:
    def clear_screen():
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')

    def verify_modules():
        for i in data.modules:
            os.system(f"pip3 install {i}")
        return
    def google(promt):
        for url in search(promt, num_results=5):
            print(url)
        sleep(10)
        return
        
    def start_command(promt):
        if promt.lower().strip() not in comamnds.commands_List:
            tool.google(promt=promt)  
            return
    
        
        for i in comamnds.commands:
            if i["user_command"] in promt.lower().strip():
                print(f"Launching {i['event']}...")
                if ".exe" in i["event"]:
                    os.system(i["event"])
                elif "https" in i["event"]:
                    os.system("start" + " " + i["event"])
                elif os.path.exists(i["event"]):
                    os.startfile(filepath=i["event"])

        return 
    
    def close_microfone(promt,data):
        if promt == "Fechar Microfone":
            ative_microfone = input("Ativar Microfone: ")
            data.Microfone_Open = False
        else:
            return

    def exit_program():
        exit()
#Project created successfully!