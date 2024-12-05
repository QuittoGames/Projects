from tool import tool
from user import user
from data import data
""". Crie um programa que leia o nome e duas notas de um(a) aluno(a). O programa deve calcular a
média dessas duas notas e saber se o aluno foi aprovado ou reprovado (média é 7.0), o
programa deve guardar tudo em uma lista. No final, o seu programa deve conseguir imprimir o
boletim de cada aluno individualmente pelos métodos de manipulação das listas (tente usar o
enumerate). Observe abaixo uma possível implementação do código:
Além disso, ao final, o seu programa deve mostrar qual a média de toda a turma e informar
quantos alunos ficaram abaixo da média da turma"""


def add_user():
    try:
        tool.clear_screen()
        name = input("Digite O Nome Do Aluno: ")
        n1 = float(input(f"Digite A 1 Nota Do {name}: "))
        n2 = float(input(f"Digite A 2 Nota Do {name}: "))
        if n1 > 10 or n1 < 0 and n2 > 10 or n2 < 0:
            return

        aluno_media = tool.media_notas(x=n1, y = n2)

        if tool.verify_aproved(media=aluno_media):
            arproved = "Aprovado"
        else:
            arproved = "Nao Aprovado"

        client = user(name=name,nota1=n1,nota2=n2,user_media = aluno_media,Aporoved=arproved)
        data.alunos.append(client)
        return
    except Exception as E:
        print(f"Erro, {E}")

def Start():
    tool.clear_screen()
    value_alunos = int(input("Digite A Quantidade De Alunos: "))
    for i in range(value_alunos):
        add_user()

    Show_Info()
    return

    
def Show_Info():
    tool.clear_screen()
    #formart_retrun_text = f"Name: {i.name}, Nota 1: {i.nota1}, Nota 2: {i.nota2}, Media: {i.user_media}, Conceito: {i.Aporoved}"
    print("* Info")
    for i in data.alunos:
        print(f"*  Name: {i.name}   , Nota 1: {i.nota1}   , Nota 2: {i.nota2}   , Media: {i.user_media}   , Conceito: {i.Aporoved}   ")
        print("\n")
    return  
        


if __name__ == "__main__":                  
    Start()         