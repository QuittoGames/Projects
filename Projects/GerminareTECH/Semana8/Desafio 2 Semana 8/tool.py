import os
import platform
from dataclasses import dataclass
import asyncio
from time import sleep

""". Construa um programa para ler as idades de 80 pessoas, calcular e mostrar a média das idades.
O programa deve mostrar também a idade da pessoa mais velha e da mais nova. Deve mostrar
ainda quantas pessoas estão em cada uma das seguintes faixas etárias:
• Bebê: até 2 anos
• Criança: de 2 a 10 anos
• Pré-adolescente: de 10 a 14 anos
• Adolescente: de 14 a 18 anos
• Jovem: de 18 a 21 anos
• Adulto: de 21 até 60 anos
• Idoso: 60 anos ou mais
"""


@dataclass
class tool:
    def clear_screen():
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')

    media = lambda data: sum(data.banco_de_dados) / len(data.banco_de_dados)

    maior_idade = lambda data: max(data.banco_de_dados)
    
    menor_idade = lambda data: min(data.banco_de_dados)

    
    def calcular_faixa_etaria(data):
        faixas = {
            'Bebê': 0,
            'Criança': 0,
            'Pré-adolescente': 0,
            'Adolescente': 0,
            'Jovem': 0,
            'Adulto': 0,
            'Idoso': 0
        }
        
        for idade in data.banco_de_dados:
            if idade <= 2:
                faixas['Bebê'] += 1
            elif 2 < idade <= 10:
                faixas['Criança'] += 1
            elif 10 < idade <= 14:
                faixas['Pré-adolescente'] += 1
            elif 14 < idade <= 18:
                faixas['Adolescente'] += 1
            elif 18 < idade <= 21:
                faixas['Jovem'] += 1
            elif 21 < idade <= 60:
                faixas['Adulto'] += 1
            else:
                faixas['Idoso'] += 1
        
        return faixas
    