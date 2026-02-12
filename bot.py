from telegram import Bot
import asyncio

## TOKEN = "SEU_TOKEN_AQUI"       # Do @BotFather
## CHAT_ID = "SEU_CHAT_ID_AQUI"   # Seu ID ou grupo

async def enviar_alerta(mensagem):
    bot = Bot(token=TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=mensagem)

# Exemplo de uso
if __name__ == "__main__":
    asyncio.run(enviar_alerta("Alerta de teste: Produtividade baixa detectada!"))
