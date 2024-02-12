from app.settings import COMPRAS_PARAGUAI_SEARCH_PAGE
import re


def items_txt_reader_to_urls(file_path: str = "docs/items.txt"):
    """
    Reads a text file and returns a list of urls.

    Args:
        file_path (str): The path to the text file.

    Returns:
        list: A list of lines from the text file, with leading and trailing whitespace removed.
    """
    lines = []
    with open(file_path, 'r') as file:
        for line in file:
            lines.append(COMPRAS_PARAGUAI_SEARCH_PAGE + re.sub(r'[\s]+', '+', line.strip().lower()))
    return lines