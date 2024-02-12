from app.utils.convert_currency_to_float import convert_currency_to_float
from app.utils.calculate_average_price import calculate_average_price
from app.concrete.aiohttp_fetch import AioHttpFetch
from app.concrete.selectolax_parser import SelectolaxParser
from selectolax.parser import HTMLParser
from app.settings import COMPRAS_PARAGUAI_URL


def get_product_name_from_url(main_url: str) -> str:
    """
    Extracts the product name from a Compras Paraguai URL.

    Args:
        url (str): The URL to extract the product name from.

    Returns:
        str: The product name extracted from the URL.
    """
    return main_url.split('/')[-2].split('_')[-2].replace('-', ' ').title()


async def compras_paraguai_async(url: str) -> dict | None:
    """
    Asynchronously fetches the content of a URL, parses it using a SelectolaxParser,
    and returns the main URL and average price of the item.

    Args:
        url (str): The URL of the item to fetch and parse.

    Returns:
        str | None: A string containing the main URL and average price of the item,
        or None if the content could not be fetched or parsed.
    """
    parser = SelectolaxParser(HTMLParser, convert_currency_to_float, calculate_average_price)
    list_item_content = await AioHttpFetch.get(url)
    if list_item_content is None: return
    temp_url = parser.compras_paraguai_item_main_url(list_item_content)
    if temp_url is None: return
    main_url = COMPRAS_PARAGUAI_URL + temp_url
    main_content = await AioHttpFetch.get(main_url)
    if main_content is None: return
    average_price = parser.compras_paraguai_item_average_price(main_content)
    return {
        "product_name": get_product_name_from_url(main_url),
        "average_price": average_price,
        "product_url": main_url
    }
