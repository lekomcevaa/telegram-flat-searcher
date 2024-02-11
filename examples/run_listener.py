import logging
from teledatastore.telegram_listener import TelegramListener
import asyncio
import os

# logging.basicConfig(level=logging.DEBUG)

listener = TelegramListener()  # Все параметры берутся из переменных окружения
asyncio.run(listener.run())
