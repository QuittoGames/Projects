from tool import tool
from time import sleep
from data import data


def Start():
    tool.clear_screen()
    try:
        minutes = int(input("Digite Os Minutos: "))
        segundos = int(input("Digite Os Segundos: "))
    except TypeError:
        print(data.colors["reset"]+"Digite Valroes Interos! ")
        Start()
        return
    
    if minutes <= 0 and segundos <= 0:
        print("Valores Invalidos!")
        Start()
        return

    try:
        tool.contagem_regresiva(min=minutes,s=segundos)
        Start()
        return
    except Exception as E:
        print(f"Erro, {E}")


if __name__ == "__main__":
    Start()