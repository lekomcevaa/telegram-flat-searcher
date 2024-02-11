from telegram_flat_searcher.telegram_listener import TelegramListener
from telegram_flat_searcher.database import Database
from telegram_flat_searcher.polling import PollingService
import asyncio

async def start_polling_service_async(db):
    polling_service = PollingService(db)
    polling_service.logger.info("Сервис поллинга запущен.")
    while True:
        polling_service.poll_new_messages()
        await asyncio.sleep(10)  # Асинхронная задержка

async def main():
    db = Database('.env')  # Инициализация класса Database
    listener = TelegramListener(env_file='.env')  # Все параметры берутся из переменных окружения

    # Запуск слушателя и сервиса поллинга параллельно
    await asyncio.gather(
        listener.run(),
        start_polling_service_async(db),
    )

if __name__ == "__main__":
    asyncio.run(main())
