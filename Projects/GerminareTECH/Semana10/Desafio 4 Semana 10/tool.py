import os
import platform
from dataclasses import dataclass
from data import data
from time import sleep

@dataclass
class tool:
    def clear_screen():
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')

    def find_user(name):
        for i in data.users:
            if i.get("name") == name:
                return i
        return
    
    def verify_tel(tel):
        if not "+55" in tel or len(tel) > 9 and len(tel) < 0: # app somente para br
            return False
        else:
            return True
        
    def add_tel():
        try:
            name = input("Digite O Nome Do User: ")
            user = tool.find_user(name=name)
            new_tel = input("Digite O Novo Tel: ")
            if not tool.verify_tel(new_tel):
                print("Numero De Telefone Invalido Tente Novamente!")
                sleep(1.5)
                return
            n_tel = user.get("N_Tels", 0)  
            n_tel += 1 
        
            user[f"Tel{n_tel}"] = new_tel
            user["N_Tels"] = n_tel
            return user
        except Exception as E:
            print(f"Erro Na Adiçao De Numero! ,Erro: {E}")
    
    def add_user():
        try:
            name = input("Digite O Nome Do Novo Usuario: ")
            tel1 = input("Digite O Numero De Telefone Do Usuario: ")
            for i in data.users:
                if i["name"] == name:
                    print("Nome Ja Esta Em Uso!")
                    return
            user = {"name":name,"Tel1":tel1,"N_Tels":0}
            data.users.append(user)
            return user
        except Exception as E:
            print(f"Erro Al Adicionar Usuario!, Erro: {E}")
    
    def remove_user():
        try:
            name = input("Digite O Nome Do Usuario: ")
            for i in data.users:
                if i["name"] == name:
                    data.users.remove(i)
            return
        except Exception as E:
            print(f"Erro Al Remover Usuario!,Erro: {E}")
        
    def view_data():
        print(f"Data: {data.users}")
        c = input("Exit: (Presione Qualquer Tecla)")
        return
    #Nao deu tempo para arrumar
    def remove_tel(tel_nun,name):
        user = tool.find_user(name=name)
        nun_remove = input("Digite O Telefone: ")
        if tool.verify_tel(nun_remove):
            print("Numero De Telefone Invalido Tente Novamente!")
            sleep(1.5)
            tool.add_tel(name=name)
            return
        