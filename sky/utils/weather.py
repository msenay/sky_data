from datetime import time


def get_time_from_average_seconds(average_seconds: float) -> time:
    """
        Convert a time given in seconds into a datetime.time object.
        This function takes a time represented in seconds (like you might
        get from an average calculation) and breaks it down into hours,
        minutes, and seconds. It then uses those values to create a
        datetime.time object.
        Parameters:
        average_seconds (float): The time to convert, represented in seconds.
        Returns:
        time: A datetime.time object that represents the input time.
    """
    average_hours = average_seconds // 3600
    average_minutes = (average_seconds % 3600) // 60
    average_seconds = (average_seconds % 3600) % 60
    average_max_temp_time = time(int(average_hours), int(average_minutes), int(average_seconds))
    return average_max_temp_time
