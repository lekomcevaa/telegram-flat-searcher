import unittest
from unittest.mock import patch

import dotenv
from config import Config

class TestConfig(unittest.TestCase):
    """
    Unit tests for the Config class.
    """

    def setUp(self):
        self.config = Config()

    def test_get_existing_key(self):
        # Mock the os.getenv function to return a specific value
        with patch('os.getenv', return_value='value'):
            result = self.config.get('KEY')
            self.assertEqual(result, 'value')

    def test_get_non_existing_key(self):
        # Mock the os.getenv function to return None
        with patch('os.getenv', return_value=None):
            result = self.config.get('KEY', default='default_value')
            self.assertEqual(result, 'default_value')

    def test_get_with_env_file(self):
        # Mock the load_dotenv function to do nothing
        with patch('dotenv.load_dotenv'):
            config = Config(env_file='.env')
            config.get('KEY')
            # Assert that load_dotenv was called with the correct argument
            dotenv.load_dotenv.assert_called_once_with('.env')

if __name__ == '__main__':
    unittest.main()