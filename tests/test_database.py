import unittest
from unittest.mock import patch

from database import Database

class TestDatabase(unittest.TestCase):
    """
    A test case class for testing the Database class.
    """

    def setUp(self):
        self.database = Database(env_file='.env')

    def tearDown(self):
        self.database.connection.close()

    def test_save_message(self):
        timestamp = '2022-01-01 12:00:00'
        sender_id = '123456789'
        message_text = 'Hello, world!'
        
        # Mock the cursor and execute method
        with patch.object(self.database.connection, 'cursor') as mock_cursor:
            mock_execute = mock_cursor.return_value.__enter__.return_value.execute
            mock_commit = self.database.connection.commit

            self.database.save_message(timestamp, sender_id, message_text)

            # Assert that the execute method was called with the correct query and parameters
            mock_execute.assert_called_once_with(
                "INSERT INTO messages (timestamp, sender_id, message_text) VALUES (%s, %s, %s)",
                (timestamp, sender_id, message_text)
            )

            # Assert that the commit method was called
            mock_commit.assert_called_once()

if __name__ == '__main__':
    unittest.main()
