import pytest
from app.utils.convert_currency_to_float import convert_currency_to_float

cases = [
    ("R$ 1.000,50", 1_000.5),
    ("R$1000,50", 1_000.5),
    ("$1000,50", 1_000.5),
    ("1000,50", 1_000.5),
    ("1.000.000,50", 1_000_000.5),
    ("R$ 1.000.000,50", 1_000_000.5),
    ("R$ 1,99", 1.99),
]


def test_convert_currency_to_float_cases():
    """
    Test convert_currency_to_float() with multiple test cases.
    """
    for currency_str, expected in cases:
        assert convert_currency_to_float(currency_str) == expected


def test_convert_currency_to_float_raises():
    """
    Test convert_currency_to_float() with invalid input.
    """
    with pytest.raises(Exception):
        convert_currency_to_float("asbcfghjkl")