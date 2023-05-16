from time import perf_counter

from scripts.weather_analysis import WeatherAnalysis

if __name__ == "__main__":
    start_time = perf_counter()
    wa = WeatherAnalysis("http://www.fifeweather.co.uk/cowdenbeath/200606.csv")
    wa.analyze_daily_max_temperatures('Outside Temperature', 'Date', 'Time')
    wa.write_filtered_dates_and_times()
    wa.forecast_next_month_temperatures()
    end_time = perf_counter()
    elapsed_time = end_time - start_time
    print(f"Analysis is finished in {elapsed_time} seconds.")
