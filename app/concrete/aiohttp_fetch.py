from app.interfaces.fetch import Fetch
import aiohttp

class AioHttpFetch(Fetch):
    @staticmethod
    async def get(url: str) -> bytes | None:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status == 200:
                        return await response.read()
                    return None
        except Exception as e:
            # TODO: Log the exception
            return None