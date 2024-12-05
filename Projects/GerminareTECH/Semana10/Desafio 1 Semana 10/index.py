from data import data
from tool import tool
from time import sleep

"""1. Crie um programa para encontrar todas as chaves que estão associadas a um determinado valor
em um dicionário. Para isso, crie uma função que receberá 2 parâmetros, o primeiro parâmetro
será um dicionário a ser analisado, e como segundo parâmetro um valor a ser buscado. A função
retornará uma lista com as chaves encontradas, essa lista pode ter diversos valores, apenas um
ou nenhum.
Exemplo:
Clientes= {
“Nome”: “Ana Maria Braga”,
 “Endereco”: “Av. Maria Augusta, s/n”,
“OperadoraCelular”: “Vivo”,
 . . .
}
Resultado esperado da função para localizar o valor “Maria”: Retornar as chaves NOME,
ENDEREÇO """


#Grillo nao vol coseguir resolver o bug porque presiso tentar terminar os demais desafios 

def Show_Info(name,data,type_veirify): # Aqui o clen code e triste
    print(f"* Infos Do Users {name}") 
    print(f"* Name: {name}")
    print(f"* Endereço: {tool.get_user_data(name=name,Type_return="endereco",Type_Verify=name)}")
    print(f"* Operadora: {tool.get_user_data(name=name,Type_return="Operadora",Type_Verify=name)}")
    sleep(5)
    Start()
    return
    

def Start():
    tool.clear_screen()
    name = input("Digite O Nome Para Pesquisa: ")
    if not tool.get_user_data(name=name,Type_return=name,Type_Verify=name,data=data):
        print("Usuario Nao Aceito!")
        return
    
    tool.clear_screen()
    print("IMPORTANTE PARA PESQUISA DE DADOS ULTILIZE OS SEGUINTES PARAMETROS! ('name': Nome , 'endereco' : Endereso Do Usuario , 'Operadora': Operadora De Celular)")
    type_return = input(f"Digite O Valor A Ser Pesquisado Do User {name}: ")
    Show_Info(name=name,data=data,type_veirify=type_return)
    return
    


if __name__ == "__main__":
    Start()