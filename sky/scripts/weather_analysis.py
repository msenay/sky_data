import pandas as pd
from pandas import DataFrame, Series

from datetime import time
from typing import Tuple, Union

from constants import MAX_ATTEMPTS, DELAY
from utils.decorators import retry
from utils.weather import get_time_from_average_seconds


class WeatherAnalysis:
    """
      A class used to analyze and forecast weather data.

      This class provides methods for performing various analyses on weather data,
      including determining the average time of the day's hottest temperature,
      finding the most common time of the day's hottest temperature, and forecasting
      future temperatures based on past patterns.

      Attributes:
          data_frame (DataFrame): A pandas DataFrame containing the weather data.

      Methods:
          load_data_from_csv -> DataFrame: Loads a CSV file from a URL into a DataFrame.
          analyze_daily_max_temperatures -> Tuple[time, str]: Analyzes the temperature data.
          write_filtered_dates_and_times -> None: Writes date and time information into a file.
          forecast_next_month_temperatures -> None: Forecasts weather based on given parameters.
      """

    def __init__(self, data: Union[str, DataFrame]) -> None:
        """
        The constructor for WeatherAnalysis class.
        The constructor checks if the data is already a pandas DataFrame. If it is, it sets the data_frame attribute
        to the given DataFrame. If it isn't, it assumes the data is a URL to a CSV file and attempts to load the CSV
        file into a DataFrame using the load_data_from_csv method.
        """

        self.data_frame: DataFrame = data if isinstance(data, pd.DataFrame) else self.load_data_from_csv(data)

    @retry(max_attempts=MAX_ATTEMPTS, delay=DELAY)
    def load_data_from_csv(self, csv_url: str) -> DataFrame:
        """
        This method uses pandas to read a CSV file from a given URL. It also combines the 'Date' and 'Time' columns
        into a single 'Datetime' column for easier analysis. It uses a retry decorator to handle possible network errors
        or temporary unavailability of the URL.
        """

        df = pd.read_csv(csv_url)
        df['Datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], dayfirst=True)
        df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
        return df

    def analyze_daily_max_temperatures(self, temp_col: str, date_col: str, time_col: str,
                                       output_file: str = 'results/q1_outside_temp_analysis.txt') -> Tuple[time, str]:
        """
        Analyze daily maximum temperatures.
        This method groups the DataFrame by date and finds the index of the maximum temperature for each day. It then
        calculates the average time of the day's maximum temperature and the most common time of the day's maximum
        temperature. The top ten hottest times on distinct days are also determined. The results are written to a file.
        """

        try:
            with open(output_file, 'w') as f:
                daily_max_temp = self.data_frame.groupby(self.data_frame[date_col].dt.date)[temp_col].idxmax()

                times = pd.to_datetime(self.data_frame.loc[daily_max_temp][time_col], format='%H:%M').dt.time
                seconds = times.apply(lambda t: t.hour * 3600 + t.minute * 60 + t.second)
                average_seconds = seconds.mean()
                average_max_temp_time = get_time_from_average_seconds(average_seconds)

                modes: Series = self.data_frame.loc[daily_max_temp][time_col].mode()
                avg_temps = [(self.data_frame[
                                  (self.data_frame["Time"] == _time) & (self.data_frame.index.isin(daily_max_temp))][
                                  temp_col].mean(), _time) for _time in modes]
                _, most_common_max_temp_time = max(avg_temps)

                top_ten_hottest_times = self.data_frame.loc[daily_max_temp].nlargest(10, temp_col)

                f.write(f'Average time of hottest daily temperature: {average_max_temp_time}\n')
                f.write(f'Most commonly occurring hottest time: {most_common_max_temp_time}\n')
                f.write('Top Ten hottest times on distinct days:\n')
                f.write(top_ten_hottest_times.to_string(index=False))

        except Exception as e:
            print(f"Error in outside_temp_analysis: {e}")
            raise e
        return average_max_temp_time, most_common_max_temp_time

    def write_filtered_dates_and_times(self, month: int = 6, day: int = 9, h_temp: float = 22.3, l_temp: float = 10.3,
                                       h_precision: float = 1, l_precision: float = 0.2,
                                       hi_temp_col: str = 'Hi Temperature',
                                       low_temp_col: str = 'Low Temperature', date_col: str = 'Date',
                                       time_col: str = 'Time',
                                       output_file: str = 'results/q2_selected_dates.txt') -> None:
        """
        Write filtered dates and times to a file.
        This method filters the DataFrame based on the month, day, high temperature, low temperature, and their
        precisions. The selected dates and times are then written to a file.
        """

        try:
            with open(output_file, 'w') as f:
                selected_dates = self.data_frame[
                    (self.data_frame[date_col].dt.month == month) & (self.data_frame[date_col].dt.day <= day) & (
                            (abs(self.data_frame[hi_temp_col] - h_temp) <= h_precision) |
                            (abs(self.data_frame[low_temp_col] - l_temp) <= l_precision))]

                f.write(selected_dates[[date_col, time_col]].to_string(index=False))
        except Exception as e:
            print(f"Error in write_date_and_time: {e}")
            raise e

    def forecast_next_month_temperatures(self, month: int = 6, day: int = 9, base_temp: float = 25,
                                         temp_col: str = 'Outside Temperature',
                                         date_col: str = 'Date', time_col: str = 'Time',
                                         output_file: str = 'results/q3_forecast.txt') -> None:
        """
        Forecast next month's temperatures based on past patterns.
        This method uses past weather patterns within a given month and day to forecast next month's temperatures.
        The temperatures are forecasted by calculating the difference between the past temperatures and their average,
        and then adding this difference to a base temperature. The forecasted temperatures are then written to a file.
        """
        try:
            with open(output_file, 'w') as f:
                month_patterns: DataFrame = self.data_frame[
                    (self.data_frame[date_col].dt.month == month) & (self.data_frame[date_col].dt.day <= day)]
                month_patterns = month_patterns.copy()
                month_patterns['Temperature Difference'] = month_patterns[temp_col] - month_patterns[temp_col].mean()
                month_forecast = month_patterns.copy()
                month_forecast[date_col] = month_forecast[date_col] + pd.DateOffset(months=1)
                month_forecast[temp_col] = base_temp + month_forecast['Temperature Difference']
                f.write(month_forecast[[date_col, time_col, temp_col]].to_string(index=False))
        except Exception as e:
            print(f"Error in forecast: {e}")
            raise e
