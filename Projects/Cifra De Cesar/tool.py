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


    def verify_mesage(m):
        if not m in data.caracteres_especiais and m in data.alfabeto:
            return True
        else:
            return False
        

    
    def crifra_cesar(m,key):
        tool.clear_screen()
        mensagem = str(m).strip()
        #if not tool.verify_mesage(m=mensagem): return
        code = "".strip()
        
        for i in mensagem:
            index_in_afabeto = data.alfabeto.index(i)
            result_index = index_in_afabeto + key % len(data.alfabeto)
            code += data.alfabeto[result_index]
        return code
    

print(tool.crifra_cesar(m ="eu amo python",key=5))