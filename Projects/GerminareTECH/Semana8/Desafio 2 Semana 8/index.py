from data import data
from tool import tool

#Grillo Ficou muito ruim este code
# este code era async porem no final vi que n avia nessesidade ent tirei

    
def Show_Info():
    print(f"Media: {tool.media(data=data)}")   
    print(f"Maior Idade: {tool.maior_idade(data=data)}")
    print(f"Menor Idade: {tool.menor_idade(data=data)}")
    print(f"Quantidade Por Idade: {tool.calcular_faixa_etaria(data=data)}")


def Start():
    tool.clear_screen()
    run_program = input("Inciar Leitura De dados: ")
    try:
        Show_Info()
        return
    except Exception as E:
        print(f"Erro, {E}")


if __name__ == "__main__":
    Start()