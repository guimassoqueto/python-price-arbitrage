import re


def convert_currency_to_float(currency_str: str):
    """
    Converts a currency string to a float value.

    Args:
        currency_str (str): The currency string to be converted.

    Returns:
        float: The float value representing the currency.

    Example:
        >>> convert_currency_to_float('R$ 1,000.50')
        1000.5
    """
    no_currency_symbol = re.sub(r'[R]?[$]?[\s]*', '', currency_str)
    no_thousands_separator = re.sub(r'\.', '', no_currency_symbol)
    standardized_decimal = re.sub(r',', '.', no_thousands_separator)
    return float(standardized_decimal)

