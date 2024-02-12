from app.utils.calculate_average_price import calculate_average_price


def test_calculate_average_price():
    """
    Test that the function returns the correct average price.
    """
    result = calculate_average_price([1, 2, 3, 4, 5])
    assert result == 3.00