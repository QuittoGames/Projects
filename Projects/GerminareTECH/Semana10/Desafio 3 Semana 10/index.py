from tool import tool
from data import data
from time import sleep

"""3. Crie uma função que recebe uma palavra, essa função deve retornar as letras únicas para a
construção desta palavra e a quantidade de cada letra utilizada.
Exemplo de entradas e saídas:
letras ("abracadabra")
"""

def Show_Info(data):
    print("* Results")
    print(f"* Letras Indetificadas: {data.select_word}")
    print(tool.Show_Info_Data(data=data))
    sleep(10)
    Start()
    return
    

def Start():
    tool.clear_screen()
    word = input("Digite Uma Palavra: ").strip()
    data_class_intance = data(select_word=[])

    result = tool.calc_words(string=word,data_istance=data_class_intance)
    Show_Info(data=data_class_intance)
    return

if __name__ == "__main__":
    Start()
