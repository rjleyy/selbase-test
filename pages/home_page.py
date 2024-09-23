from seleniumbase import BaseCase
from config.default import BASE_URL
from utils.helper import assert_list_text


class HomePage:

    def __init__(self, sb: BaseCase):

        # Locators
        self.sb = sb
        self.search_input = ".search-active"
        self.search_placeholder = "[placeholder='Search']"
        self.search_button = ".button-search"
        self.product_link = ".main-menu li:nth-child(2)"
        self.about_link = ".footer-list ul li:nth-child(1) a"
        self.copyright_link = ".copyright p a"
        self.nav_links = ".main-menu li"

    def open(self):
        self.sb.open(BASE_URL)

    def search_for_item(self, item):
        self.sb.click(self.search_input)
        self.sb.type(self.search_placeholder, item)
        self.sb.click(self.search_button)



    def verify_nav_links(self, expected_nav_text):
        """
        Verifies the text of nav links with expected texts.
        :param expected_nav_text:

        """
        assert_list_text(self.sb, self.nav_links, expected_nav_text)
        #for i, text in enumerate(expected_nav_text, start=1):
        #    self.sb.assert_text(text, f"{self.nav_links}:nth-child({i})")
