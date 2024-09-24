from seleniumbase import BaseCase
from pages.home_page import HomePage
from utils.helper import assert_list_text
import pytest
import requests
from specs.base_test import BaseTest


class TestHomePage(BaseTest):
    """
    Page object class for Home Page
    Encapsulates all interactions with Home Page
    """

    def setUp(self, masterqa_mode=False):
        # This will call the parent class when needed
        super().setUp()
        self.homepage = HomePage(self)
        self.homepage.open()

    def tearDown(self):
        print("Log Out")
        super().tearDown()

    @pytest.mark.smoke
    def test_verify_page_title_and_url(self):
        # assert url and title contains SDET Unicorns
        self.assert_url_contains("sdetunicorns")
        self.assert_title_contains("SDET Unicorns")

    # new definitions for search test functions
    @pytest.mark.search
    def test_search_flow(self):
        homepage = HomePage(self)
        # This function clicks on the search input field.
        homepage.search_for_item("Lenovo")
        # assert to see if the Showing Results text is visible
        self.assert_text_visible("Showing Results for Lenovo")

    @pytest.mark.search
    def test_search_flow_with_xpath(self):

        homepage = HomePage(self)
        homepage.open()
        # This function clicks on the search input field.
        self.click("//button[@class='search-active']")
        # Type 'Lenovo' the search field input
        self.type("//input[@placeholder='Search']", "Lenovo")
        # Click on search button to enter the search
        self.click("//button[@class='button-search']")
        # assert to see if the Showing Results text is visible
        self.assert_text_visible("Showing Results for Apple")

    def test_nav_links(self):
        homepage = HomePage(self)
        self.assert_text("Products", homepage.product_link)
        expected_nav_text = [
            "Home",
            "Products",
            "About Us",
            "Contact",
            "Upload",
        ]

        homepage.verify_nav_links(expected_nav_text)

    def test_about_link(self):
        homepage = HomePage(self)
        # click on the About Us link in the main-menu
        self.click(homepage.about_link)
        # ALSO CAN BE SHOWN AS THIS self.click(".footer-list [href='/about']")
        # Verify that the url contains "about"
        self.assert_url_contains("about")

    def test_product_categories(self):
        homepage = HomePage(self)
        # click on the Product page link in the main menu
        self.click(homepage.product_link)
        # create a list of category items in the products page
        category_items = ["All Categories", "Laptop", "Electronics", "Keyboard"]
        # create a loop that checks all links are present in the category items
        assert_list_text(self, ".sidebar-widget-list.mt-30 li", category_items)
        # for i, text in enumerate(category_items, start=1):
        # self.assert_text(text, f".sidebar-widget-list.mt-30 li:nth-child({i})")
        # verify that the categories on the left side of the screen are listed on the page

    def test_new_tab(self):
        homepage = HomePage(self)
        # Before state for tabs
        print(self.driver.window_handles)
        self.click(homepage.copyright_link)
        # After state for tabs
        print(self.driver.window_handles)
        # Index into the tab list
        self.switch_to_tab(1)
        # Assert that you are on the new tab
        self.assert_title_contains("Master Software Testing and Automation")
        # Switch back to original position
        self.switch_to_default_tab()
        self.assert_title_contains("Practice with React")
