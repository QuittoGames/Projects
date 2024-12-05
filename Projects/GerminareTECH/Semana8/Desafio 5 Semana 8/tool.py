import os
import platform
from dataclasses import dataclass
from time import sleep
from data import data

@dataclass
class tool:
    def clear_screen():
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')


    def contagem_regresiva(min,s): # ficou umm polco confuso mais deu certo 
        try:
            for m in range(min,-1,-1):
                if m == min:
                    sec = s
                else:
                    sec = 59
                while sec > 0:
                    sec -=1 
                    if sec <= 10:
                        format_nunber =  data.colors["Red"] + f"{min}:{sec}"
                    else:
                        format_nunber = data.colors["Ciano"]+ f"{min}:{sec}"

                    print(format_nunber)
                    sleep(1)
                    data.colors["reset"]
        except Exception as E:
            print(f"Erro No Loop: {E}")

        format_nunber = data.colors["reset"]
        return
        