import os
import platform
from dataclasses import dataclass

"""3. Crie uma função que recebe uma palavra, essa função deve retornar as letras únicas para a
construção desta palavra e a quantidade de cada letra utilizada.
Exemplo de entradas e saídas:
letras ("abracadabra")
"""


@dataclass
class tool:
    def clear_screen():
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')
    
    def get_value_word(word,data):
        try:
            for i in data.afabeto:
                if i["word"] == word:
                    return i
            return
        except Exception as E:
            print(f"Erro Na Coleta De Dados!, Erro: {E}")

    def calc_words(string,data_istance):
        selct_words = []
        try:
            for i in string:
                word = tool.get_value_word(word=i,data=data_istance)
                word["value"] += 1
                selct_words.append(i)
            return data_istance
        except Exception as E:
            print(f"Erro No Calculo De Letras!, Erro: {E}")
        
    def Show_Info_Data(data):
        for i in data.afabeto:
            #if i["word"] in data.select_word: nao tava rodando devido que a arry n ta sendo passada para coletar infos porem n cosgue arrumar
            print(f"* Letra: {i['word']}, Quantidade de Vezes: {i['value']}")
        return
    
