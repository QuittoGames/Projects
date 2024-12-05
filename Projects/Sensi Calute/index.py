from tool import tool
from time import sleep

def Start():
    try:
        tool.clear_screen()
        DPI = float(input("Digite A Sua DPI: "))
        value_sensi = float(input("Digite A Sensibilidade: "))
        tool.clear_screen()
        print(f"* Resultado: {tool.Sensi_calc(DPI=DPI,value_sensi=value_sensi)}")
        sleep(5)
        Start()
        return
    except Exception as E:
        print(f"Erro, {E}")

if __name__ == "__main__":
    Start()