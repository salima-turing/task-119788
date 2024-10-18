import pytest
def aggregate_data(data):
    """
    Aggregates data by calculating the mean of a list of numbers.

    Args:
        data (list): A list of numbers.

    Returns:
        float: The mean of the numbers in the list.

    Raises:
        ValueError: If the list is empty.
        TypeError: If the list contains non-numeric values.
    """
    if not data:
        raise ValueError("Cannot calculate mean of an empty list.")

    for value in data:
        if not isinstance(value, (int, float)):
            raise TypeError("All values must be numeric.")

    total_sum = sum(data)
    mean = total_sum / len(data)

    return mean
