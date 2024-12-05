from PyQt6.QtWidgets import QWidget, QPushButton, QLabel, QFrame, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QPropertyAnimation, QEasingCurve,QTimer
class UI:
    @staticmethod
    def create_button(parent, text, x, y, width, height, color):
        """Cria um botão estilizado com animação ao passar o mouse."""
        button = QPushButton(text, parent)
        button.setGeometry(x, y, width, height)
        button.setStyleSheet(f"""
            QPushButton {{
                background-color: {color};
                color: white;
                border-radius: 8px;
                font-size: 14px;
                padding: 8px 16px;
                border: 1px solid #005A9E;
                transition: all 0.3s ease;
            }}
            QPushButton:hover {{
                background-color: #005A9E;
                transform: scale(1.05);
            }}
            QPushButton:pressed {{
                background-color: #004578;
                color: #D1E8FF;
            }}
        """)
        return button

    @staticmethod
    def create_label(parent, text, x, y, font_size, color):
        """Cria um texto estilizado com transições."""
        label = QLabel(text, parent)
        label.move(x, y)
        label.setStyleSheet(f"""
            QLabel {{
                color: {color};
                font-size: {font_size}px;
                font-weight: bold;
                background-color: transparent;
                transition: opacity 0.5s ease;
            }}
        """)
        return label

    @staticmethod
    def create_window(resX, resY, title, logo_path, bg_color):
        """Cria a janela principal com bordas arredondadas e sombra."""
        window = QWidget()
        window.resize(resX, resY)
        window.setWindowTitle(title)
        window.setWindowIcon(QIcon(logo_path))
        window.setStyleSheet(f"""
            QWidget {{
                background-color: {bg_color};
                border-radius: 12px;
                box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.3);
            }}
        """)
        return window

    @staticmethod
    def add_frame(parent, x, y, width, height, color):
        """Adiciona um frame estilizado com animação."""
        frame = QFrame(parent)
        frame.setGeometry(x, y, width, height)
        frame.setStyleSheet(f"""
            QFrame {{
                background-color: {color};
                border-radius: 8px;
                box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.2);
            }}
        """)
        return frame

    @staticmethod

    def animate_widget(widget, property_name, start_value, end_value, duration, delay=0):
        # A animação será feita sobre a propriedade 'opacity' ou qualquer outra que você deseje animar.
        animation = QPropertyAnimation(widget, property_name.encode("utf-8"))

        # Definir os valores de início e fim
        animation.setStartValue(start_value)
        animation.setEndValue(end_value)
        
        # Definir a duração da animação
        animation.setDuration(duration)

        # Definir a curva de animação
        animation.setEasingCurve(QEasingCurve.Type.OutCubic)

        # Adicionando o atraso usando QTimer para iniciar a animação após o delay
        if delay > 0:
            QTimer.singleShot(delay, lambda: animation.start())
        else:
            animation.start()

