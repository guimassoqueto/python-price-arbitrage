from typing import List


def calculate_average_price(price_list: List[float]):
    """
    Calculate the average price from a list of prices.

    Args:
        price_list (List[float]): A list of prices.

    Returns:
        float: The average price rounded to 2 decimal places.
    """
    average_price = sum(price_list) / len(price_list)
    return round(float(average_price), 2)