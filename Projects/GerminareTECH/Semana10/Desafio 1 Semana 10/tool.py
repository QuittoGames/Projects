import os
import platform
from dataclasses import dataclass

@dataclass
class tool:
    def clear_screen():
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')

    def get_user_data(Type_return,Type_Verify,name,data):
        for i in data.users:
            if i[Type_Verify] == Type_Verify:
                return i[Type_return]
            
        return None