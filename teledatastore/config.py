from dotenv import load_dotenv
import os

class Config:
    def __init__(self, env_file=None):
        """
        Initializes a Config object.

        Args:
            env_file (str, optional): Path to the .env file. Defaults to None.
        """
        if env_file:
            load_dotenv(env_file)
        else:
            load_dotenv()

    def get(self, key, default=None):
        """
        Retrieves the value of the specified environment variable.

        Args:
            key (str): The name of the environment variable.
            default (str, optional): Default value to return if the environment variable is not found. Defaults to None.

        Returns:
            str: The value of the environment variable, or the default value if not found.
        """
        return os.getenv(key, default)
