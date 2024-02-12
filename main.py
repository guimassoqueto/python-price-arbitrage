import asyncio
from app.main.compras_paraguai import compras_paraguai_async
from app.utils.items_txt_reader_to_urls import items_txt_reader_to_urls


async def main(urls: list[str] = None):
    tasks = [asyncio.wait_for(compras_paraguai_async(url), timeout=10) for url in urls]
    for future in asyncio.as_completed(tasks):
        content = await future
        if content is not None:
            print(content)
        continue


if __name__ == "__main__":
    try:
        urls = items_txt_reader_to_urls()
        asyncio.run(main(urls))
    except Exception as e:
        print(e)
