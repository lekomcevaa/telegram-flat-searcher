import time
from .database import Database
from .utils.logger import setup_logger
from .utils.logger import setup_logger  # Импорт функции настройки логгера

class PollingService:
    def __init__(self, db):
        """
        Initialize the PollingService class.

        Args:
            db: The database object.

        Attributes:
            db: The database object.
            logger: The logger object for this class.
            last_checked_id: The last processed ID.
        """
        self.db = db
        self.logger = setup_logger(self.__class__.__name__)
        self.last_checked_id = self.get_last_processed_id()
        self.logger.debug("PollingService инициализирован")
    

    def get_last_processed_id(self):
        """
        Get the last processed ID from the database.

        Returns:
            int: The last processed ID.
        """
        self.logger.debug("Получение последнего обработанного ID.")
        result = self.db.execute_query("SELECT MAX(id) FROM messages WHERE processed = 1")
        last_id = result[0][0] if result else 0  # Получаем первый элемент первой строки результата, если он есть
        try:
            last_id = int(last_id)
        except (ValueError, TypeError):
            last_id = 0
        self.logger.debug(f"Последнй обработанный ID: {last_id}, при result {result}.")
        return last_id

    def poll_new_messages(self):
        """
        Poll for new messages from the database and process them.
        """
        self.logger.debug(f"Проверка наличия новых сообщений. last_checked_id: {self.last_checked_id}")
        # Используем новый метод execute_query для выполнения запроса
        new_messages = self.db.execute_query("SELECT * FROM messages WHERE id > %s AND processed = 0", (self.last_checked_id,))
        if new_messages:
            for record in new_messages:
                self.process_new_record(record)

    def process_new_record(self, record):
        """
        Process a new record from the database.

        Args:
            record: The record to process.
        """
        self.logger.debug(f"Обработка новой записи: {record}")
        # После обработки обновляем статус и последний обработанный ID
        self.db.execute_query("UPDATE messages SET processed = 1 WHERE id = %s", (record[0],))
        self.last_checked_id = record[0]
        self.logger.debug(f"Обработка записи завершена, обновлен последний обработанный ID: {self.last_checked_id}")

