from data import data
from tool import tool
from filter_parameters import FilterParameters

"""• Crie uma função que receba a lista de clientes e os seguintes critérios de filtro como
argumentos:
o Idade mínima e máxima desejada para os clientes.
o Localização desejada (por exemplo, cidade ou estado).
o Valor mínimo de compras realizadas pelos clientes"""

def Show_Info(data_local):
    print("* Result")
    print(f"* Filter: {data.filter_clients}")

def Start():
    local_class_data = data()

    tool.clear_screen()
    name = input("Digite O Nome: ")
    idade_min = int(input("Digite A Idade Minima: "))
    idade_max = int(input("Digite A Idade Maxima: "))

    if 0 > idade_min or idade_min > idade_max:
        print("Erro: A idade mínima deve ser maior que 0 e menor que a idade máxima. Por favor, insira os valores corretamente!")
        Start()
        return  

    location = str(input("Digite A Localiçao: "))
    if location not in data.locations:
        print("Localização Nao Encotrada")
        Start()
        return  

    value_min_buy = float(input("Digite O Valor Minimo De Vendas: "))
    if value_min_buy < 0:
        print("Erro!")
        Start()
        return    
    parameters = FilterParameters(name= name,idade_max=idade_max,idade_min=idade_min,location=location,value_min=value_min_buy)

    tool.filter_data(data=local_class_data,parameters=parameters)

    Show_Info(data_local = local_class_data)
    return

if __name__ == "__main__":
    Start()