from dataclasses import dataclass


@dataclass
class data:
    clientes = [    # o mano temm que deletar a conta se ele trocar de cidade 
    ("Alice", 30, "São Paulo", 500),  
    ("Bob", 25, "Rio de Janeiro", 300),
    ("Carol", 35, "São Paulo", 700),
    ("David", 40, "Brasília", 1000),
    ("Eva", 28, "Rio de Janeiro", 400),
]
    filter_clients = []
    locations = ["São Paulo","Rio de Janeiro","Brasília"]
