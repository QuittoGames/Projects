import os
import platform
from dataclasses import dataclass
from data import data
from time import sleep

"""A Escola Germinare Business registra um aumento de 10% no número de alunos a cada ano,
enquanto a Escola Germinare TECH apresenta um crescimento populacional de 50% ao ano.
Supondo que essas taxas de crescimento se mantenham constantes e que a Escola Germinare
TECH comece com uma quantidade de alunos menor do que a Escola Germinare Business,
escreva um programa que permita ao usuário inserir a quantidade atual de alunos em ambas as
escolas e calcular em quantos anos a Escola Germinare TECH ultrapassará a Escola Germinare
Business em número de alunos"""



@dataclass
class tool:
    def clear_screen():
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')

    calc_porcentagem_tech = lambda tech : tech * (1 + 0.5) 
    calc_porcentagem_business= lambda bussiness : bussiness * (1 + 0.1) 

    def calc_populacao(data):
        years = 0 
        while data.tech_p < data.business_p:
            data.tech_p = tool.calc_porcentagem_tech(tech=data.tech_p)
            data.business_p = tool.calc_porcentagem_business(bussiness=data.business_p)
            years +=1
            if data.tech_p >= data.business_p:
                return years
                break
            else:
                continue
            
    def verify_value(x):
        if x <= 0:
            print("Valor Invalido!")
            sleep(2)
            return False
        else:
            return True
                
