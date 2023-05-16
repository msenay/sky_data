import time
from functools import wraps


def retry(max_attempts: int = 5, delay: int = 5):
    """
    A decorator that allows a function to retry execution if an exception is raised during its execution.

    Parameters:
    max_attempts (int): The maximum number of execution attempts before the function gives up. Default is 5.
    delay (int): The number of seconds to wait between each retry attempt. Default is 5.

    Returns:
    function: The decorated function that will retry execution upon failure.

    Example Usage:
    @retry(max_attempts=3, delay=2)
    def some_function():
        ...
    """

    def decorator_retry(func):
        @wraps(func)
        def wrapper_retry(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f"Error occurred: {e}")
                    print(f"Attempt {attempts} of {max_attempts} failed. Retrying in {delay} seconds...")
                    time.sleep(delay)
            print("Failed after maximum attempts. Exiting.")
            exit()

        return wrapper_retry

    return decorator_retry
