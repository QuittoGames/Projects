from tool import tool
from time import sleep

"""4. Escreva um programa para armazenar uma agenda de telefones em um dicionário. Cada pessoa
pode ter um ou mais telefones e a chave do dicionário é o nome da pessoa. Seu programa deve
ter as seguintes funções:
incluirNovoTel – essa função acrescenta um novo nome na agenda, com um ou mais telefones.
Ela deve receber como argumentos o nome e os telefones.
incluirTelefone – essa função acrescenta um telefone em um nome existente na agenda. Caso
o nome não exista na agenda, você deve incluí-lo, use a função anterior para incluir o novo nome.
excluirTelefone – essa função exclui um telefone de uma pessoa que já está na agenda. Se a
pessoa tiver apenas um telefone, a pessoa deve ser excluída da agenda.
excluirNome – essa função exclui uma pessoa da agenda. """


def Start():
    tool.clear_screen()
    print("* Vivo Maneger")
    print("1. Add Tel For User")
    print("2. Add User")
    print("3. Remove User")
    print("4. View Data")
    print("5. Exit")
    opition = input("Digite Sua Opiçao: ")
    if opition == "1":
        tool.clear_screen()
        print(tool.add_tel())
        sleep(2)
        Start()
        return
    elif opition == "2":
        tool.clear_screen()
        print(tool.add_user())
        sleep(2)
        Start()
        return
    elif opition == "3":
        tool.clear_screen()
        print(tool.remove_user())
        sleep(2)
        Start()
        return
    elif opition == "4":
        tool.clear_screen()
        tool.view_data()
        Start()
        return
    elif opition == "5":
        return
    else:
        print("Comando Invalido!")
        sleep(2)
        Start()
        return
if __name__ == "__main__":
    Start()