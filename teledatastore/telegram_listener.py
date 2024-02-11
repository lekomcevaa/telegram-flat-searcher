from telethon import TelegramClient, events
from .database import Database
from .logger import setup_logger
from .config import Config
from telethon import events
from telethon.sessions import StringSession

class TelegramListener:
    """
    A class that listens for new messages in a Telegram group and saves them to a database.

    Args:
        group_name_or_id (str, optional): The name or ID of the Telegram group to listen to. If not provided, it will be fetched from the environment configuration.
        env_file (str, optional): The path to the environment file containing the necessary configuration. Defaults to '.env'.

    Attributes:
        client (TelegramClient): The Telegram client used for authentication and message retrieval.
        db (Database): The database object used for saving messages.
        logger (Logger): The logger object used for logging events and errors.

    Methods:
        run: Starts the listener and waits for new messages.

    """

    def __init__(self, group_name_or_id=None, env_file='.env'):
        """
        Initializes a new instance of the TelegramListener class.

        Args:
            group_name_or_id (str, optional): The name or ID of the Telegram group to listen to. If not provided, it will be fetched from the environment configuration.
            env_file (str, optional): The path to the environment file containing the necessary configuration. Defaults to '.env'.
        """
        config = Config(env_file)
        self.logger = setup_logger(self.__class__.__name__)

        # Load environment variables using Config
        api_id = config.get('TELEGRAM_API_ID')
        api_hash = config.get('TELEGRAM_API_HASH')
        self.group_name_or_id = group_name_or_id or config.get('TELEGRAM_GROUP_ID')
        session_string = config.get('TELEGRAM_SESSION_STRING', default=None)


        # Initialize Telegram client and database object
        self.client = TelegramClient(StringSession(session_string), api_id, api_hash) # type: ignore
        self.db = Database(env_file)
        self.logger.debug("TelegramListener initialized")

    async def run(self):
        """
        Starts the listener and waits for new messages.
        """
        @self.client.on(events.NewMessage(chats=self.group_name_or_id))
        async def new_message_listener(event):
            self.logger.info(f"Received new message from {event.sender_id}")
            timestamp = event.date
            sender_id = event.sender_id
            message_text = event.message.message
            try:
                self.save_message_to_db(timestamp, sender_id, message_text)
                self.logger.info(f'Message from {sender_id} saved.')
            except Exception as e:
                self.logger.error(f'Failed to save message from {sender_id}: {e}')

        self.logger.debug("Starting authentication")
        await self.client.start() # type: ignore
        self.logger.debug("Authentication completed")
        await self.client.run_until_disconnected() # type: ignore

    def save_message_to_db(self, timestamp, sender_id, message_text):
        """
        Saves a message to the database.

        Args:
            timestamp (datetime): The timestamp of the message.
            sender_id (int): The ID of the message sender.
            message_text (str): The text of the message.
        """
        self.db.save_message(timestamp, sender_id, message_text)
        print(f'Message from {sender_id} saved.')
