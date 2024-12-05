from dataclasses import  dataclass

""" Faça um programa que ajude as pessoas a saberem o tempo necessário para comprar sua casa
própria fazendo um investimento fixo mensal. O programa deve ler o valor do imóvel, o valor do
investimento mensal e a taxa mensal de juros. Caso o valor do investimento mensal seja menor
do que 1% do valor do imóvel deve ser mostrada uma mensagem informando não ser viável o
investimento. O tempo necessário para compra deve ser calculado em meses utilizando juros
compostos."""


@dataclass
class data:
    value_imovel: float
    i: float
    taxa_mensal: float
