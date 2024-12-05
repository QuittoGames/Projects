from tool import tool
from data.data import data
from data.user import user
from time import sleep

"""As lojas da Swift estão com uma promoção na qual é dado um desconto no total da compra de
acordo com a quantidade de produtos escolhidos, desde que o valor total da compra não seja
menor que 100 reais. Os descontos são os seguintes: quatro produtos têm desconto de 4%,
cinco produtos têm desconto de 8%, e seis ou mais produtos têm desconto de 12%.
Escreva um programa em Python que solicite ao usuário:
• A quantidade de produtos que deseja comprar, garantindo que seja um valor maior que zero.
• O preço de cada produto, também garantindo que seja um valor maior que zero.
• O programa deve calcular o valor total da compra sem desconto, o percentual e o valor do
desconto aplicado, e o valor a pagar com desconto. Todos os valores referentes a dinheiro
devem ser apresentados com duas casas decimais"""

# Grilo Nao Deu tempo de terminar mais ja fiz um  muito parecido e ta no meu git hub ele e meio antigo mais ainda fuciona tinha deeixado para refatorar porem n fiz ainda https://github.com/QuittoGames/Restaurant-System


def Start():
    tool.clear_screen()
    nun_products = int(input("Digite A Quantidade De Produtos: "))
    for i in range(nun_products):
        tool.clear_screen()
        menu()
        return

def menu():
    try:
        for index, produto in enumerate(data.produtos):
            print(f"{index}: {produto["name"]} , R$ {produto["price"]:.2f}")

        client_opition = input("Digite Sua Opiçao : ")
    except Exception as E:
        print(f"Erro No Input, {E}")

    try:
        tool.clear_screen()
        data_name = tool.get_data_item(data=data,type_return="name",name=client_opition)
        if data_name == client_opition:
            user.client_products.append(client_opition)
        else:
            print("Produtos Nao Indentificado !")
            sleep(2)
            Start()
            return
    except Exception as E:
        print("Erro No Banco De Dados!")
        return

if __name__ == "__main__":
    Start()