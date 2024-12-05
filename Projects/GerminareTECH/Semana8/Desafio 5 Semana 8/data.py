from colorama import Fore, Back, Style, init
from dataclasses import dataclass

init() 
@dataclass
class data:
    colors = {
        "reset": Style.RESET_ALL,
        "Blue": Fore.BLUE,
        "Red": Fore.RED,
        "Ciano": Fore.CYAN,
}
    
