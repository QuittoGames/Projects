from dataclasses import dataclass
import os
from data import data


@dataclass
class comamnds:
    commands = [{"user_command": "spotify", "event": "Spotify.exe"},
        {"user_command": "chrome", "event": "chrome.exe"},
        {"user_command": "gpt", "event": "https://chatgpt.com/"},
        {"user_command": "chat gpt", "event": "https://chatgpt.com/"},
        {"user_command": "arquivos", "event": "explorer.exe"},
        {"user_command": "explorer", "event": "explorer.exe"},
        {"user_command": "cmd", "event": "cmd.exe"},
        {"user_command": "notas", "event": "notepad.exe"},
        {"user_command": "calculator", "event": "calc.exe"},
        {"user_command": "calculadora", "event": "calc.exe"},
        {"user_command": "discord", "event": "discord.exe"},
        {"user_command": "zoom", "event": "zoom.exe"},
        {"user_command": "firefox", "event": "firefox.exe"},
        {"user_command": "vscode", "event": "code"},
        {"user_command": "codigo", "event": "code"},
        {"user_command": "zap", "event": "https://web.whatsapp.com/"},
        {"user_command": "WhatsApp", "event": "https://web.whatsapp.com/"},
        {"user_command": "Simpsons Ao Vivo", "event": "https://www.twitch.tv/tv_amarela"},
        {"user_command": "Os Simpsons Ao Vivo", "event": "https://www.twitch.tv/tv_amarela"},
        {"user_command": "Simpsons", "event": "https://www.twitch.tv/tv_amarela"},
        {"user_command": "python ide", "event": "https://www.twitch.tv/tv_amarela"},
        {"user_command": "twitch", "event": "https://www.twitch.tv"},
        {"user_command": "fortnite tracker", "event": "https://fortnitetracker.com"},
        {"user_command": "paint", "event": "mspaint.exe"},
        {"user_command": "word", "event": "winword.exe"},
        {"user_command": "excel", "event": "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.exe"},
        {"user_command": "powerpoint", "event": "powerpnt.exe"},
        {"user_command": "git bash", "event": "git-bash.exe"},
        {"user_command": "desligar", "event": "shutdown -s -t 0"},
        {"user_command": "reiniciar", "event": "shutdown -r -t 0"},
        {"user_command": "trava tela", "event": "rundll32.exe user32.dll, LockWorkStation"},
        {"user_command": "github", "event": "https://github.com"},
        {"user_command": "stack overflow", "event": "https://stackoverflow.com"},
        {"user_command": "google", "event": "https://www.google.com"},
        {"user_command": "Twitter", "event": "https://twitter.com"},
        {"user_command": "Twitter", "event": "https://twitter.com"},
        {"user_command": "Twitter", "event": "https://twitter.com"},
        {"user_command": "dark mode", "event": r"C:\Users\gusta\Downloads\Projects\WindowsDark\StartPC.reg"},
        {"user_command": "light mode", "event": r"C:\Users\gusta\Downloads\Projects\WindowsDark\LightMode.reg"},
        {"user_command": "downloads", "event": r"C:\Users\gusta\Downloads"},
        {"user_command": "imagens", "event": r"C:\Users\gusta\Pictures"},
        {"user_command": "documentos", "event": r"C:\Users\gusta\Documents"},
        {"user_command": "videos", "event": r"C:\Users\gusta\Videos"},
        #{"user_command": "pause música", "event": "nircmd.exe mediaplaypause"},
        {"user_command": "iniciar projeto", "event": r"C:\Users\gusta\Downloads\Projects\ProjectSetup\index.py"},
        {"user_command": "gerenciador de tarefas", "event": "taskmgr.exe"},
        {"user_command": "configurações", "event": "ms-settings:"},
        {"user_command": "windows update", "event": "ms-settings:windowsupdate"},
        {"user_command": "painel de controle", "event": "control.exe"},
        {"user_command": "informações do sistema", "event": "msinfo32.exe"},

        #{"user_command": "epic games", "event": "EpicGamesLauncher.exe"},




        



        ]
    
    commands_List = [
        "spotify",
        "chrome",
        "gpt",
        "chat gpt",
        "arquivos",
        "explorer",
        "cmd",
        "notas",
        "calculator",
        "calculadora",
        "discord",
        "zoom",
        "firefox",
        "vscode",
        "codigo",
        "zap",
        "WhatsApp",
        "Simpsons Ao Vivo",
        "Os Simpsons Ao Vivo",
        "Simpsons",
        "python ide",
        "twitch",
        "fortnite tracker",
        "paint",
        "word",
        "excel",
        "powerpoint",
        "git bash",
        "desligar",
        "reiniciar",
        "trava tela",
        "github",
        "stack overflow",
        "google",
        "Twitter",
        "dark mode",
        "light mode",
        "downloads",
        "imagens",
        "documentos",
        "videos",
        "iniciar projeto",
        "gerenciador de tarefas",
        "configurações",
        "windows update",
        "painel de controle",
        "informações do sistema",
]
