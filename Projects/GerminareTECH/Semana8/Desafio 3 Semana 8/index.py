from tool import tool
from data import data

"""A Escola Germinare Business registra um aumento de 10% no número de alunos a cada ano,
enquanto a Escola Germinare TECH apresenta um crescimento populacional de 50% ao ano.
Supondo que essas taxas de crescimento se mantenham constantes e que a Escola Germinare
TECH comece com uma quantidade de alunos menor do que a Escola Germinare Business,
escreva um programa que permita ao usuário inserir a quantidade atual de alunos em ambas as
escolas e calcular em quantos anos a Escola Germinare TECH ultrapassará a Escola Germinare
Business em número de alunos"""


def Show_Info(local_data):
    year = tool.calc_populacao(data=local_data)
    print("_"* 30 + "Info" + "_" * 30)
    print(f"* Em {year} Anos E O TECH Alcasara O Bussiness")
    print(f"* TECH: {local_data.tech_p}")
    print(f"* Bussiness: {local_data.business_p}")
    return


def Start():
    tool.clear_screen()
    print("O TECH deve ser menor que o Business!")
    tech = int(input("Digite A Quantidade De Alunos Do Gerinare TECH: "))
    if not tool.verify_value(x =tech):
        Start()
        return
    business = int(input("Digite A Quantidade De Alunos Do Gerinare Business: "))
    if not tool.verify_value(x =business):
        Start()
        return
        
    if tech >= business: 
        print("Valor Nao Pode Ser Aceito!")
        Start()
        return
    local_data = data(tech_p= tech, business_p= business)
    Show_Info(local_data=local_data)
    return


if __name__ == "__main__":
    Start()