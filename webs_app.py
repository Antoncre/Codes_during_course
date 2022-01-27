import requests
import logging
import asyncio
import aiohttp
import async_timeout
import time


logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d]%(message)s',
                    level=logging.INFO,
                    datefmt='%d-%m-%Y %H:%M:%S',
                    filename='logs.txt'
                    )

logger = logging.getLogger('scraping')

logger.info("loading a books list...")


from web_pages.books_page import BooksPage
page_content = requests.get('https://books.toscrape.com').content
page = BooksPage(page_content)

loop = asyncio.get_event_loop()

books = page.sheet


async def fetch_page(session, url):
    page_start = time.time()
    async with async_timeout.timeout(10):
        async with session.get(url) as response:
            print(f"page {url} took {time.time() - page_start} time")
            return await response.text()


async def get_multiple_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        grouped_tasks = asyncio.gather(*tasks)
        return await grouped_tasks

urls = ['https://books.toscrape.com/catalogue/page-{x+1}.html' for i in range(1, page.page_count)]
start = time.time()
pages = loop.run_until_complete(get_multiple_pages(loop, *urls))
print(f'Total page requests took {time.time() - start}')


for page.content in pages:
    logger.debug('Creating a Bookspage from page content.')
    page = BooksPage(page_content)
    books.extend(page.sheet)
