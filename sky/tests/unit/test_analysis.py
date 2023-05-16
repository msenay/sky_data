import unittest
import pandas as pd
import os

from scripts.weather_analysis import WeatherAnalysis


class TestWeatherDataFunctions(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            'Hi Temperature': [22.5, 22.3, 10.1, 10.3, 22.3, 10.3, 24.6, 23.1, 25.8, 24.3],
            'Low Temperature': [10.3, 10.3, 22.3, 22.3, 10.3, 22.3, 15.2, 16.7, 14.3, 15.8],
            'Outside Temperature': [9.8, 9.4, 9.5, 9.6, 9.5, 9.5, 25.5, 24.5, 26.5, 25.5],
            'Date': pd.to_datetime(
                ['31/05/2006', '31/05/2006', '31/05/2006', '01/06/2006', '01/06/2006', '01/06/2006', '02/06/2006',
                 '02/06/2006', '03/06/2006', '03/06/2006'], dayfirst=True),
            'Time': ['23:30', '23:40', '23:50', '00:00', '00:10', '00:20', '12:00', '12:10', '12:00', '12:10']
        })
        self.weather_analysis = WeatherAnalysis(self.df)
        self.output_file_1 = 'test_output.txt'
        self.output_file_2 = 'test_dates.txt'
        self.output_file_3 = 'test_forecast.txt'

    def test_outside_temp_analysis(self):
        self.weather_analysis.analyze_daily_max_temperatures('Outside Temperature', 'Date', 'Time',
                                                             self.output_file_1)
        with open(self.output_file_1, 'r') as f:
            lines = f.readlines()
        self.assertEqual(lines[0], 'Average time of hottest daily temperature: 11:52:30\n')
        self.assertEqual(lines[1], 'Most commonly occurring hottest time: 12:00\n')

    def test_write_date_and_time(self):
        self.weather_analysis.write_filtered_dates_and_times(month=6, day=1, h_temp=22.3, l_temp=10.3,
                                                             h_precision=1,
                                                             l_precision=0.2,
                                                             hi_temp_col='Hi Temperature',
                                                             low_temp_col='Low Temperature',
                                                             date_col='Date', time_col='Time',
                                                             output_file=self.output_file_2)
        with open(self.output_file_2, 'r') as f:
            lines = f.readlines()
        self.assertEqual(len(lines), 2)  # There should be 1 dates + header line

    def test_forecast(self):
        self.weather_analysis.forecast_next_month_temperatures(month=6, day=1, base_temp=25,
                                                               temp_col='Outside Temperature',
                                                               date_col='Date', time_col='Time',
                                                               output_file=self.output_file_3)
        with open(self.output_file_3, 'r') as f:
            lines = f.readlines()
        self.assertEqual(len(lines), 4)  # There should be 3 dates + header line in the file

    def tearDown(self):
        # Remove the output files after the tests
        if os.path.exists(self.output_file_1):
            os.remove(self.output_file_1)
        if os.path.exists(self.output_file_2):
            os.remove(self.output_file_2)
        if os.path.exists(self.output_file_3):
            os.remove(self.output_file_3)


if __name__ == '__main__':
    unittest.main()
