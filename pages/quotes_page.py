from typing import List
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

from locators.quotes_page_locators import QuotesPageLocators
from parsers.quote import QuoteParser


class QuotesPage:
    def __init__(self, browser):
        self.browser = browser

    @property
    def quotes(self) -> List[QuoteParser]:
        return [
            QuoteParser(e)
            for e in self.browser.find_elements_by_css_selector(
                QuotesPageLocators.QUOTE
            )
        ]

    @property
    def all_authors(self) -> Select:
        elements = self.browser.find_element_by_css_selector(QuotesPageLocators.AUTHOR)
        return Select(elements)


    def find_author(self,author_name: str):
        self.all_authors.select_by_visible_text(author_name)

    @property
    def all_tags(self) -> Select:
        tags = self.browser.find_element_by_css_selector(QuotesPageLocators.TAGS)
        return Select(tags)

    def find_tag(self, tag_name: str):
        self.all_tags.select_by_visible_text(tag_name)

    def get_available_tags(self) -> List[str]:
        return [tag.text.strip() for tag in self.all_tags.options]

    @property
    def button(self):
        button = self.browser.find_element_by_css_selector(QuotesPageLocators.BUTTON)
        return button

    def search_quotes(self,author: str,tag: str):
        self.find_author(author)

        WebDriverWait(self.browser, 10).until(
            expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, QuotesPageLocators.TAGS_DROPDOWN)
            )
        )


        try:
            self.find_tag(tag)
        except NoSuchElementException:
            raise InvalidAuthorTagError(
                f'This Author {author} have no quotes tagged {tag}'
            )

        self.button.click()
        return self.quotes


class InvalidAuthorTagError(ValueError):
    pass