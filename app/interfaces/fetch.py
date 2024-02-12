from abc import ABC, abstractmethod
from typing import Tuple


class Fetch(ABC):
    @staticmethod
    @abstractmethod
    async def get(url: str) -> bytes | None:
        """
        Fetch the content of a given URL.
        Returns the content of the URL.
        """
        pass