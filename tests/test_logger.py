import unittest
import logging
from unittest.mock import patch

from logger import setup_logger


class TestLogger(unittest.TestCase):
    """
    A test case class for testing the setup_logger function.
    """

    def test_setup_logger(self):
        # Mock the getLogger method
        with patch('logger.logging.getLogger') as mock_get_logger:
            mock_logger = mock_get_logger.return_value

            # Call the setup_logger function
            logger = setup_logger('test_logger')

            # Assert that getLogger was called with the correct name
            mock_get_logger.assert_called_once_with('test_logger')

            # Assert that the logger level was set to DEBUG
            mock_logger.setLevel.assert_called_once_with(logging.DEBUG)

            # Assert that a StreamHandler was added to the logger
            mock_logger.addHandler.assert_called_once()

            # Assert that the logger returned is the same as the mock logger
            self.assertEqual(logger, mock_logger)


if __name__ == '__main__':
    unittest.main()