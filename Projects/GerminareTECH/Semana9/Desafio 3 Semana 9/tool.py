import os
import platform
from dataclasses import dataclass
from data import data
from filter_parameters import FilterParameters


"""• Crie uma função que receba a lista de clientes e os seguintes critérios de filtro como
argumentos:
o Idade mínima e máxima desejada para os clientes.
o Localização desejada (por exemplo, cidade ou estado).
o Valor mínimo de compras realizadas pelos clientes"""

@dataclass
class tool:
    def clear_screen():
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')

    def filter_data(data,parameters):
        user = tool.get_user_for_name(name= parameters.name)

        if not user:
            print(f"Cliente {parameters.name} não encontrado.")
            return
        
        verify_value = 0 
        if parameters.idade_min < user[1] < parameters.idade_max:
            verify_value += 1
        elif parameters.value_min < user[2]:
            verify_value += 1
        elif parameters.location != None:
            verify_value += 1

        if verify_value == 3:
            user = [parameters.name,parameters.idade_min,parameters.idade_max,parameters.value_min,parameters.location]
            data.filter_clients.append(user)
            return

    def get_user_for_name(name):
        for i in data.clientes:
            if i[0] == name:
                return name, [i[1],i[2],i[3]]
        return []