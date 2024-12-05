from dataclasses import dataclass
import platform

@dataclass
class data:
        modules = ["os","PyQt6"]
        OS = platform.system()
        resolutionX = 1000
        resolutionY = 1000
        basicBtnLarge = 200
        basicBtnAltura = 35
