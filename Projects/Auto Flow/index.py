from PyQt6.QtWidgets import QApplication, QGraphicsOpacityEffect
from PyQt6.QtCore import QThread, pyqtSignal, QPropertyAnimation, QRect, QEasingCurve, QTimer
from PyQt6.QtGui import QIcon
from data import data
from tool import tool
from UI import UI
from time import sleep
import speech_recognition as sr
import sys

app = QApplication(sys.argv)

def Start():
    tool.clear_screen()

    # Criando janela principal
    main_window = UI.create_window(
        data.resolutionX,
        data.resolutionY,
        "AutoFlow + Ecosystem",
        "logo.png",
        data.secondaryColor
    )

    # Adicionando título com animação de opacidade
    title_label = UI.create_label(main_window, "Bem-vindo ao AutoFlow", 20, 20, 24, data.textColor)
    
    # Aplicando a animação de opacidade usando QGraphicsOpacityEffect
    opacity_effect = QGraphicsOpacityEffect()
    title_label.setGraphicsEffect(opacity_effect)
    opacity_animation = QPropertyAnimation(opacity_effect, b"opacity")
    opacity_animation.setStartValue(0.0)
    opacity_animation.setEndValue(1.0)
    opacity_animation.setDuration(1000)
    opacity_animation.start()

    # Criando área de aplicativos
    app_frame = UI.add_frame(main_window, 20, 80, 860, 500, color="#252525")

    # Criando botões manualmente com posições ajustadas
    button_width = 250
    button_height = 60
    button_y = 40

    # Botões com animação
    devflow_btn = UI.create_button(app_frame, "DevFlow", 40, button_y, button_width, button_height, data.themeColor)
    UI.animate_widget(devflow_btn, b"geometry", QRect(40, button_y, button_width, button_height), QRect(40, button_y, button_width, button_height), 1000)
    button_y += 80

    chat_gpt_btn = UI.create_button(app_frame, "Chat GPT", 40, button_y, button_width, button_height, data.themeColor)
    UI.animate_widget(chat_gpt_btn, b"geometry", QRect(40, button_y, button_width, button_height), QRect(40, button_y, button_width, button_height), 1000)
    button_y += 80

    ollama_ai_btn = UI.create_button(app_frame, "Ollama AI", 40, button_y, button_width, button_height, data.themeColor)
    UI.animate_widget(ollama_ai_btn, b"geometry", QRect(40, button_y, button_width, button_height), QRect(40, button_y, button_width, button_height), 1000)
    button_y += 80

    # Adicionando botão para iniciar o reconhecimento de voz
    voice_button = UI.create_button(
        app_frame,
        "Iniciar Voz",
        40,
        button_y,
        button_width,
        button_height,
        data.themeColor,
    )

    # Configurando o comportamento do botão
    voice_thread = VoiceController()

    def handle_voice_command(command):
        print(f"Comando de voz recebido: {command}")
        tool.display_message(app_frame, f"Comando: {command}", 20, 300, 500, 50)

    voice_thread.voice_output.connect(handle_voice_command)

    def start_voice_recognition():
        if not voice_thread.isRunning():
            data.Microfone_Open = True
            voice_thread.start()
            print("Reconhecimento de voz iniciado.")
        else:
            print("Reconhecimento de voz já em execução.")

    voice_button.clicked.connect(start_voice_recognition)

    # Rodando o app
    main_window.show()
    app.exec()

class VoiceController(QThread):
    voice_output = pyqtSignal(str)  

    def voice_command(self):
        rec = sr.Recognizer()
        tool.clear_screen()
        print("Microfone Iniciado")
        while data.Microfone_Open:
            try:
                with sr.Microphone(0) as mic:
                    rec.adjust_for_ambient_noise(mic)
                    print("Aguardando áudio...")
                    audio = rec.listen(mic)
                    command = rec.recognize_google(audio, language=data.language)
                    tool.start_command(command)
                    tool.close_microfone(prompt=command, data=data)
                    print("Prompt recebido: " + command)
                    sleep(1)
            except Exception as E:
                print(f"Erro no loop de áudio: {E}")
                self.voice_command()  # Chamada recursiva se houver erro

if __name__ == "__main__":
    tool.verify_modules()
    Start()
