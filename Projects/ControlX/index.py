import inputs
from tool import tool
from data import data
import asyncio

def Start():
    pass

async def start_program():
    print("Atualizando dependências...")
    tool.clear_screen()
    await tool.wait_animetion(tool.verfy_modules)  # Aguarda a animação e instalação
    Start()

if __name__ == "__main__":
    asyncio.run(start_program())