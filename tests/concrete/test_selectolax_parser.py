#TODO: create tests for the SelectolaxParser class
from unittest.mock import Mock
from app.concrete.selectolax_parser import SelectolaxParser


def make_selectolax_parser() -> SelectolaxParser:
    """
    Creates and returns an instance of SelectolaxParser.

    This function takes no arguments and returns an instance of SelectolaxParser.
    The SelectolaxParser instance is created with a currency_to_float function and a calculate_average_price function.

    Returns:
        SelectolaxParser: An instance of SelectolaxParser.
    """
    calculate_average_price = Mock()
    currency_to_float = Mock()
    html_parser = Mock()
    return SelectolaxParser(html_parser, currency_to_float, calculate_average_price)


def test_selectolax_should_call_htmlparser_with_correct_arg():
    """
    Test case to verify that the Selectolax parser calls the HTML parser with the correct argument.
    """
    parser = make_selectolax_parser()
    content = b"content"
    parser.compras_paraguai_item_average_price(content)
    parser.html_parser.assert_called_once_with(content)


# TODO: create tests