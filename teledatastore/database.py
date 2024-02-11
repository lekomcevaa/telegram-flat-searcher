import mysql.connector
from .logger import setup_logger
from .config import Config  # Импортируем класс Config

class Database:
    """
    Represents a database connection.

    Args:
        env_file (str, optional): The path to the environment file. Defaults to '.env'.
    """

    def __init__(self, env_file='.env'):
        config = Config(env_file)  # Создаем экземпляр Config
        self.logger = setup_logger(self.__class__.__name__)
        self.connection = mysql.connector.connect(
            host=config.get('DB_HOST'),  # Получаем параметры из Config
            user=config.get('DB_USER'),
            password=config.get('DB_PASSWORD'),
            database=config.get('DB_NAME')
        )
        self.logger.debug("Database подключение инициализировано")


    
    def save_message(self, timestamp, sender_id, message_text):
        """
        Save a message to the database.

        Args:
            timestamp (str): The timestamp of the message.
            sender_id (str): The ID of the message sender.
            message_text (str): The text of the message.
        """
        # Логгирование попытки сохранения сообщения
        self.logger.info(f"Сохранение сообщения от {sender_id}")
        cursor = self.connection.cursor()
        query = "INSERT INTO messages (timestamp, sender_id, message_text) VALUES (%s, %s, %s)"
        cursor.execute(query, (timestamp, sender_id, message_text))
        self.connection.commit()
