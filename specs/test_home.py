from seleniumbase import BaseCase
from pages.home_page import HomePage

class TestHomePage(BaseCase):
    def test_verify_page_title_and_url(self):
        homepage = HomePage(self)
        homepage.open()
    # assert url and title contains SDET Unicorns
        self.assert_url_contains("sdetunicorns")
        self.assert_title_contains("SDET Unicorns")

    # new definitions for search test functions

    def test_search_flow(self):
        homepage = HomePage(self)
        homepage.open()
        # This function clicks on the search input field.
        homepage.search_for_item('Lenovo')
        # assert to see if the Showing Results text is visible
        self.assert_text_visible("Showing Results for Lenovo")

    def test_search_flow_with_xpath(self):
        self.open("https://practice-react.sdetunicorns.com/")
        # This function clicks on the search input field.
        self.click("//button[@class='search-active']")
        # Type 'Lenovo' the search field input
        self.type("//input[@placeholder='Search']", "Lenovo")
        # Click on search button to enter the search
        self.click("//button[@class='button-search']")
        # assert to see if the Showing Results text is visible
        self.assert_text_visible("Showing Results for Lenovo")

    def test_nav_links(self):
        homepage = HomePage(self)
        homepage.open()
        self.assert_text("Products", homepage.product_link)
        expected_nav_text = ["Home", "Products", "About Us", "Contact", "Upload", ]
        homepage.verify_nav_links(expected_nav_text)

    def test_about_link(self):
        homepage = HomePage(self)
        homepage.open()
        # click on the About Us link in the main-menu
        self.click(homepage.about_link)
        # ALSO CAN BE SHOWN AS THIS self.click(".footer-list [href='/about']")
        # Verify that the url contains "about"
        self.assert_url_contains("about")

    def test_product_categories(self):
        homepage = HomePage(self)
        homepage.open()
        # click on the Product page link in the main menu
        self.click(homepage.product_link)
        # create a list of category items in the products page
        category_items = ["All Categories", "Laptop", "Electronics", "Keyboard"]
        # create a loop that checks all links are present in the category items
        for i, text in enumerate(category_items, start=1):
            self.assert_text(text, f".sidebar-widget-list.mt-30 li:nth-child({i})")
        # verify that the categories on the left side of the screen are listed on the page

    def test_new_tab(self):
        homepage = HomePage(self)
        homepage.open()
        # Before state for tabs
        print(self.driver.window_handles)
        self.click(homepage.copyright_link)
        # After state for tabs
        print(self.driver.window_handles)
        # Index into the tab list
        self.switch_to_tab(1)
        # Assert that you are on the new tab
        self.assert_title_contains('Master Software Testing and Automation')
        # Switch back to original position
        self.switch_to_default_tab()
        self.assert_title_contains('Practice with React')


