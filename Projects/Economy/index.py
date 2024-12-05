from data.data import data
from tool import tool
from user import user
import openpyxl

#Varieveis Globlias
wb = openpyxl.Workbook()

file = None

ws = wb.active

def Start():
    local_user = user(saldo= int, investido= int, despesas= int, lucro= int, saldo_liquido= int)
    if tool.verify_extetion_file():
        file = openpyxl.load_workbook(data.Diretory_file)
        if data.Debug: print("Verificaçao Concluida!")
        user_data_set = tool.set_infos(local_user,ws)
        main(user_local= user_data_set)
        return
    else:
        # Create new file if it doesn't exist
        wb.save(data.Diretory_file)
        user_data_set = tool.set_infos(local_user,ws)
        main(user_local=user_data_set)
        return
    


def main(user_local):
    tool.clear_screen()
    print("* Economy Controler")
    print("="*30)
    print(f"* Saldo: {user_local.saldo}")
    print(f"* Saldo Investido: {user_local.investido}")
    print(f"* Despesas: {user_local.despesas}")
    print(f"* Lucro: {user_local.lucro}")
    print(f"* Saldo Liquido: {user_local.saldo_liquido}")



if __name__ == "__main__":
    Start()