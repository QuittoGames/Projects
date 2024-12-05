from tool import tool
from time import sleep

def Start():
    tool.clear_screen()
    print("1. Buy")
    c = input("Digite A Sua Opição: ")
    if c != "1": 
        print("Opição Invalida!")
        sleep(2)
        Start()
        return
    set_buy_setings()
    return
    
def set_buy_setings():
    tool.clear_screen()
    valor = int(input("Digite O Valor Da Compra: "))
    if valor <= 0: return
    name_user = input("Digite O Nome Do Usuario: ")
    print(tool.buy(valor=valor,name_user=name_user))
    sleep(10)
    Start()
    return

if __name__ == "__main__":
    Start()