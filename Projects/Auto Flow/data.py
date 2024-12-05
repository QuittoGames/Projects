from dataclasses import dataclass

@dataclass
class data:
    resolutionX = 900
    resolutionY = 600
    basicBtnWidth = 150
    basicBtnHeight = 40
    fontPath = r"fonts\\Font.ttf"
    language = "pt-BR"
    themeColor = "#0078D4"  # Azul padrão
    secondaryColor = "#1A1A1A"
    textColor = "#EAEAEA"

    modules = ["PyQt6"]
    Microfone_Open = True
