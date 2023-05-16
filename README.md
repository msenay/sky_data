# Weather Analysis Python Project
Introduction
This project contains Python scripts for analyzing and predicting weather patterns based on historical weather data. 
The core functionalities include finding the hottest time of the day, selecting certain dates and times based on 
temperature criteria, and forecasting future temperatures based on historical patterns.

Classes and Methods
The main class in this project is WeatherAnalysis which encapsulates all the functionalities. 

The class includes the following methods:
__init__(self, data: Union[str, DataFrame]): Initializes the class with a DataFrame or a URL pointing to a CSV file 
containing the weather data.

load_data_from_csv(self, csv_url: str): This method is used to load weather data from a CSV file.

analyze_daily_max_temperatures: This method analyzes the outside temperature data and writes the results to a file. 
It returns the average time of the hottest temperature of the day and the most common hottest time of the day.

write_filtered_dates_and_times: This method selects certain dates and times based on the temperature criteria and 
writes the selected dates and times to a file.

forecast_next_month_temperatures: This method forecasts future temperatures based on historical weather patterns and 
writes the forecasted temperatures to a file.

How to use
To use this project, you can create an instance of the WeatherAnalysis class with a DataFrame or a URL pointing to a 
CSV file containing the weather data as input. Then, you can call the methods described above on the class instance to 
analyze the weather data and make forecasts.

Dependencies
pandas
datetime
typing
Note
Please make sure to handle all the exceptions properly as the methods in the WeatherAnalysis class can raise exceptions 
when an error occurs. The methods are already designed to print the error message when an exception is raised.

The project also includes a unit test script (TestWeatherDataFunctions) to test the functionalities of 
the WeatherAnalysis class.

To Run the tests
python -m unittest discover

To run the main.py in order to get the results in results directory
python3 main.py

Conclusion
This project provides an easy-to-use tool for analyzing and predicting weather patterns based on historical weather data. 
It is designed to be flexible and robust, allowing users to easily customize the analysis and forecasting processes 
according to their needs.