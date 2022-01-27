import re
import logging
from web_locators.book_locators import BookLocators

logger = logging.getLogger('scraping.book')



class BookParser:
    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }
    def __init__(self, parent):
        logger.debug(f'New book parser created from `{parent}`.')
        self.parent = parent

    def __repr__(self):
        return f'<Book: "{self.title}", that costs: {self.price}, with star rating: {self.star_rating}>'

    @property
    def title(self):
        logger.debug("Finding a book name...")
        locator = BookLocators.NAME
        item_link = self.parent.select_one(locator)
        item_name = item_link.attrs['title']
        logger.debug(f"Found book name, `{item_name}`")
        return item_name

    @property
    def price(self):
        logger.debug("Finding a book price...")
        locator = BookLocators.PRICE
        item_price = self.parent.select_one(locator).string
        pattern = '£([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, item_price)
        float_price = float(matcher.group(1))
        logger.debug(f"Found price `{float_price}`")
        return float_price

    @property
    def star_rating(self):
        logger.debug("Finding a book star rating...")
        locator = BookLocators.STAR_RATING
        star_rating_tag = self.parent.select_one(locator)
        classes = star_rating_tag.attrs['class']
        rating_classes = [r for r in classes if r != 'star-rating']
        rating_number = BookParser.RATINGS.get(rating_classes[0])
        logger.debug(f"Found star rating, `{rating_number}`")
        return rating_number
