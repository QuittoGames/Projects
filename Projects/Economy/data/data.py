from dataclasses import dataclass


@dataclass
class data:
    file_regiter = "data.xlsx"
    files_for_execel = [".xlsx"]
    nun_verify = 1
    Debug = True
    Diretory_file = rf"C:\Users\gusta\Downloads\Projects\Economy\data\{file_regiter}"

@dataclass
class Execel_Ids:
    Saldo_id = "A2"
    Investido_id = "D2"
    Despesas_id = "C2"
    Lucro = "B2"
    Saldo_Liquido_id = "E2"