from selenium.webdriver.common.by import By
from locators.quote_locators import QuoteLocators


class QuoteParser:
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<Quote {self.content}, by {self.author}>'

    @property
    def content(self):
        JUST_LOCATOR = By.CSS_SELECTOR, QuoteLocators.CONTENT_LOCATOR
        return self.parent.find_element(*JUST_LOCATOR).text

    @property
    def author(self):
        JUST_LOCATOR = By.CSS_SELECTOR, QuoteLocators.AUTHOR_LOCATOR
        return self.parent.find_element(*JUST_LOCATOR).text

    @property
    def tags(self):
        JUST_LOCATOR = By.CSS_SELECTOR, QuoteLocators.TAGS_LOCATOR
        return self.parent.find_elements(*JUST_LOCATOR)
