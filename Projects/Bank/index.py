from data import data
from tool import tool
from user import user

def Login():
    try:
        name = input("Digite O Nome Do Usuario: ")
        if not tool.verify_user(name):
            print("Usuario Nao Encotrado!")
    except Exception as E:
        returna

def Start():
    local_user = user()

if __name__ == "__main__":
    Start()