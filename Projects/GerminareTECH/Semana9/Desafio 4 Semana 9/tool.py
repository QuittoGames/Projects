import os
import platform
from dataclasses import dataclass
from data import data

@dataclass
class tool:
    def clear_screen():
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')

    def add_car():
        name_car = input("Digite O Nome Do Carro: ")
        Kml = int(input("Digte A Quantidade De KM/L: "))
        car_regiter = {"name": name_car , "kml": Kml}
        data.carrs.append(car_regiter)
        return
    
    def calc_result(): # ficou bem ruin porque tava sem tempo 
        cosumed_cars = []
        for i in data.carrs:
            kml = i["kml"]
            name = i["name"]
            cosumed = data.distance / kml
            consume_regieter = {"name":name,"use":cosumed}
            cosumed_cars.append(cosumed_cars)
            total_cost = cosumed * data.fuel_price
            print(f"Carro: {i['name']}, Litros consumidos: {cosumed}, Custo: R$ {total_cost}")
            return
        for i in cosumed_cars:
            print(f"O Mais Economico E: {min(cosumed_cars, key=lambda x: x["use"])}") # tive que usar o chat tentei de tudo mais n queria usar lambda mais foi nessesario 