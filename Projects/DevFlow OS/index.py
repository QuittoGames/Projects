from data import data
from tool import tool
from UI import UI
from PyQt6.QtWidgets import QApplication
import sys
###import asyncio

def strat_program():
    tool.verify_moudules()
    Start()
    return

app = QApplication(sys.argv)
def Start():
    Window = UI.create_window(resX=data.resolutionX,resY=data.resolutionY,Logo_path="")
    Title = UI.create_text(x=500 , y= 100, txt= "Dev Flow OS",screm= Window)

    DevFlow_Link = UI.create_btn(X=500 , Y= 180, L= data.basicBtnLarge, A=data.basicBtnAltura, txt= "Dev Flow",screm=Window)

    Window.show()
    app.exec()



if __name__ == "__main__":
    strat_program()