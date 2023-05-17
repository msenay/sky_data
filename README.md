# Weather Analysis Python Project


### **Introduction**

This project is a Python-based weather data analysis and forecasting tool. 
It is capable of processing historical weather data to extract insights and predict future trends. 
Core functionalities include identifying the hottest times of the day, filtering dates and times based on specific 
temperature conditions, and forecasting future temperatures based on past patterns.


### **Classes and Methods**

The core component of the project is the **_WeatherAnalysis_** class, which encapsulates all functionalities.

The **_WeatherAnalysis_** class includes the following methods:

* __init__(self, data: Union[str, DataFrame]): Initializes the class with a DataFrame or a URL pointing to a CSV file containing the weather data.

* load_data_from_csv(self, csv_url: str): Loads weather data from a CSV file.

* analyze_daily_max_temperatures(): Analyzes the outside temperature data and writes the results to a file. Returns the average time of the hottest temperature of the day and the most common time of hottest temperature.

* write_filtered_dates_and_times(): Selects dates and times based on specific temperature criteria, writing the selected dates and times to a file.

* forecast_next_month_temperatures(): Forecasts future temperatures based on historical weather patterns, writing the forecasted temperatures to a file.


### **How to use**

To use this project, you can create an instance of the WeatherAnalysis class with a DataFrame or a URL pointing to a 
CSV file containing the weather data as input. Then, you can call the methods described above on the class instance to 
analyze the weather data and make forecasts.


### **Dependencies**

This project requires Python 3.6+ and the following Python libraries installed:

pandas
numpy

To install these libraries and other dependencies, you can use the provided requirements.txt file. 
In your terminal, navigate to the project directory and run the following command:

`pip install -r requirements.txt`


#### To run the main.py in order to get the results in results directory

`python3 main.py`


### Note

Please make sure to handle all the exceptions properly as the methods in the WeatherAnalysis class can raise exceptions 
when an error occurs. The methods are already designed to print the error message when an exception is raised.

The project also includes a unit test script (TestWeatherDataFunctions) to test the functionalities of 
the WeatherAnalysis class and also includes test for utils and decorators.


#### To Run the tests
`python -m unittest discover`


### **Conclusion**

This project provides an easy-to-use tool for analyzing and predicting weather patterns based on historical weather data. 
It is designed to be flexible and robust, allowing users to easily customize the analysis and forecasting processes 
according to their needs.