from data import data
from tool import tool
from time import sleep

""" Faça um programa que ajude as pessoas a saberem o tempo necessário para comprar sua casa
própria fazendo um investimento fixo mensal. O programa deve ler o valor do imóvel, o valor do
investimento mensal e a taxa mensal de juros. Caso o valor do investimento mensal seja menor
do que 1% do valor do imóvel deve ser mostrada uma mensagem informando não ser viável o
investimento. O tempo necessário para compra deve ser calculado em meses utilizando juros
compostos."""

#Grillo n entidi o uso do juros , eu ate fiz a fomula mais n usei

data_client = data(value_imovel=0,i=0,taxa_mensal=0)

def Start():
    tool.clear_screen()
    try:
        value_imovel = float(input("Digite O Valor Do Imovel: "))
        if value_imovel < 0:
            print("Valor Invalido, Tente Novamente")
            Start()
            return
        investment_value = float(input("Digite O Valor Do Investimento: "))
        if value_imovel < 0:
            print("Valor Invalido, Tente Novamente")
            Start()
            return
        taxa_mesal = float(input("Digite a Taxa Mensal, (Digite O Valor Sem A Porcentagem): ")) / 100
        if investment_value < 0.01 * value_imovel:
            print("Investimento inviável! O valor do investimento mensal deve ser maior que 1% do valor do imóvel.")
            sleep(5)
            Start()
            return
    
        data_client = data(value_imovel=value_imovel,i=investment_value,taxa_mensal=taxa_mesal)
        Show_Result(data=data_client)
        return
    except Exception as E:
        print(f"Erro, {E}")


def Show_Result(data):
    tool.clear_screen()
    try:
        valor_acumulado = 0
        meses = 0
        for _ in range(600):
            valor_acumulado += data.i  
            valor_acumulado += valor_acumulado * data.taxa_mensal  
            
            meses += 1 
            
            if valor_acumulado >= data.value_imovel: 
                print(f"Você conseguirá comprar o imóvel em {meses} meses.")
                sleep(5)
                Start()
                break
        else:
            print("Após 50 anos, o valor acumulado ainda não é suficiente para comprar o imóvel.")
            sleep(5)
            Start()
            return
    except Exception as E:
        print(f"Erro: {E}")
        sleep(5)
        Start()

if __name__ == "__main__":
    Start()