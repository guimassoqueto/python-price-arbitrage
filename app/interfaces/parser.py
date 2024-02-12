from abc import ABC, abstractmethod


class Parser(ABC):
    @abstractmethod
    def compras_paraguai_item_average_price(content: str | bytes) -> float:
        """
        Calculate the average price of an item based on the given content.

        Args:
            content (str | bytes): The content to parse and calculate the average price from.

        Returns:
            float: The average price of the item.
        """
        pass

    @abstractmethod
    def compras_paraguai_item_main_url(content: bytes) -> str | None:
        """
        Extracts the main URL of the item from the given URL.

        Args:
            content (bytes): The HTML content of the page.

        Returns:
            str: The main URL of the item.
        """
        pass
