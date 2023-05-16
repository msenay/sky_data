import unittest
from datetime import time
from utils.weather import get_time_from_average_seconds


class TestGetTimeFromAverageSeconds(unittest.TestCase):

    def test_get_time_from_average_seconds(self):
        # Test case 1: 3600 seconds = 1 hour
        result = get_time_from_average_seconds(3600)
        self.assertEqual(result, time(1, 0, 0))

        # Test case 2: 3661 seconds = 1 hour, 1 minute, 1 second
        result = get_time_from_average_seconds(3661)
        self.assertEqual(result, time(1, 1, 1))

        # Test case 3: 0 seconds = 0 hours, 0 minutes, 0 seconds
        result = get_time_from_average_seconds(0)
        self.assertEqual(result, time(0, 0, 0))


if __name__ == '__main__':
    unittest.main()
