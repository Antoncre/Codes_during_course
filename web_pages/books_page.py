import re
import logging
from bs4 import BeautifulSoup

from web_locators.books_page_locators import BooksPageLocators
from web_parsers.book import BookParser

logger = logging.getLogger('scraping.books_page')


class BooksPage:
    def __init__(self, page):
        logger.debug('Parsing page content with BeautifulSoup HTML parser.')
        self.soup = BeautifulSoup(page, 'html.parser')


    @property
    def sheet(self):
        logger.debug(f"Finding all books in the page using '{BooksPageLocators.NAME}'")
        locator = BooksPageLocators.NAME
        book_tags = self.soup.select(locator)
        return [BookParser(e) for e in book_tags]

    @property
    def page_count(self):
        logger.debug("Finding all number of catalogue pages avaliable")
        content = self.soup.select_one(BooksPageLocators.PAGER).string
        logger.info(f'found number of catalogue pages available: "{content}".')
        pattern = 'Page [0-9]+ of ([0-9]+)'
        reg = re.search(pattern, content)
        pages = int(reg.group(1))
        logger.debug(f"Extracted number of pages as integer: '{pages}'.")
        return pages
