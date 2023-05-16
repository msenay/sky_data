import unittest
from unittest.mock import patch, call
from utils.decorators import retry


class RetryDecoratorTest(unittest.TestCase):
    @patch('time.sleep', return_value=None)  # Mock sleep to avoid waiting during tests
    @patch('builtins.print')  # Mock print to avoid print statements during tests
    @patch('builtins.exit', side_effect=Exception('Exit called'))  # Mock exit and make it raise an Exception
    def test_retry(self, mock_exit, mock_print, mock_sleep):
        # This function always raises an exception
        @retry(max_attempts=3, delay=1)
        def function_that_always_fails():
            raise Exception('An error')

        with self.assertRaises(Exception) as e:
            function_that_always_fails()

        self.assertEqual(str(e.exception), 'Exit called')
        # Check if the function was attempted max_attempts times
        self.assertEqual(mock_print.call_count, 2 * 3 + 1)  # Each attempt prints two messages plus one final message
        self.assertEqual(mock_sleep.call_count, 3)  # sleep is called once after each failed attempt
        mock_sleep.assert_has_calls([call(1)] * 3)  # Check if sleep was called with correct delay


if __name__ == '__main__':
    unittest.main()
