import mysql.connector
from .utils.logger import setup_logger
from .utils.config import Config  # Импортируем класс Config

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
        self.execute_query("SET SESSION transaction_isolation='READ-COMMITTED'")
        self.logger.debug("Database подключение инициализировано")

    def get_cursor(self):
            """
            Returns a cursor object for executing database queries.
            
            Returns:
                cursor: A cursor object for executing database queries.
            """
            return self.connection.cursor()
    
    def execute_query(self, query, params=None):
            """
            Executes the given SQL query with optional parameters.

            Args:
                query (str): The SQL query to execute.
                params (tuple, optional): The parameters to be used in the query. Defaults to None.

            Returns:
                list or None: If the query is a SELECT statement, returns a list of fetched results.
                              Otherwise, returns None.

            Raises:
                mysql.connector.Error: If there is an error executing the query.

            """
            with self.connection.cursor() as cursor:
                try:
                    cursor.execute(query, params or ())
                    if query.lower().startswith("select"):
                        return cursor.fetchall()  # Возвращаем результаты для SELECT запроса
                    else:
                        self.connection.commit()  # Делаем commit для изменяющих данные запросов
                        return True
                except mysql.connector.Error as e:
                    self.connection.rollback()  # Откат изменений в случае ошибки
                    self.logger.error(f"Ошибка при выполнении запроса: {e}")
                    return None

    
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
        query = "INSERT INTO messages (timestamp, sender_id, message_text) VALUES (%s, %s, %s)"
        params = (timestamp, sender_id, message_text)
        result = self.execute_query(query, params)
        if result is True:
            self.logger.debug("Сообщение успешно сохранено.")
        else:
            self.logger.error("Ошибка при сохранении сообщения.")

