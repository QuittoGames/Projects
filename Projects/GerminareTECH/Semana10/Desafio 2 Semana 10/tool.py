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

    #Acabou nen presisando
    def find_user(Type_return,name):
        for i in data.users:
            if i["name"] == name:
                return i[Type_return]
        return "User Nao Encotrado"
    
    calc_media = lambda Values: sum(Values) / len(Values)

    def buy_action(user,valor):
        user["transasoes"] =+ 1
        user["saldo"] =- valor
        media_arry = user["media_arry"]
        media_arry.append(valor)
        meida = tool.calc_media(Values=media_arry)
        user["media"] = meida
        return

    def buy(valor,name_user):
        for i in data.users:
            if i["name"] == name_user:
                user = i
        
        tool.buy_action(user=user,valor=valor)
        return user
    

