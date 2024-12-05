from data import data
from tool import tool

def Start():
    tool.clear_screen()
    nun_veiculos = int(input("Digite A Quantidade De Veiculos: "))
    for i in range(nun_veiculos):
        tool.add_car()
    
    tool.calc_result()
    return

if __name__ == "__main__":
    Start()