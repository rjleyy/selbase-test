from seleniumbase import BaseCase

class TestHomePage(BaseCase):
    def test_verify_page_title_and_url(self):
    # open home page
        self.open("https://practice-react.sdetunicorns.com/")

    # assert url and title contains SDET Unicorns
        self.assert_url_contains("sdetunicorns")
        self.assert_title_contains("SDET Unicorns")

    # new definitions for search test functions

    def test_search_flow(self):
        self.open("https://practice-react.sdetunicorns.com/")
        # This function clicks on the search input field.
        self.click(".search-active")
        # Type 'Lenovo' the search field input
        self.type("[placeholder='Search']", "Lenovo")
        # Click on search button to enter the search
        self.click(".button-search")
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
        self.open("https://practice-react.sdetunicorns.com/")
        self.assert_text("Products", ".main-menu li:nth-child(2)")
        # create a list with all of the links
        expected_nav_text = ["Home", "Products", "About Us", "Contact", "Upload", ]
        for i, text in enumerate(expected_nav_text, start=1):
            self.assert_text(text, f".main-menu li:nth-child({i})")

    def test_about_link(self):
        self.open("https://practice-react.sdetunicorns.com/")
        # click on the About Us link in the main-menu
        self.click(".footer-list ul li:nth-child(1) a")
        # Verify that the url contains "about"
        self.assert_url_contains("about")

    def test_product_categories(self):
        self.open("https://practice-react.sdetunicorns.com/")
        # click on the Product page link in the main menu
        self.click(".main-menu li:nth-child(2)")
        # create a list of category items in the products page
        category_items = ["All Categories", "Laptop", "Electronics", "Keyboard"]
        # create a loop that checks all links are present in the category items
        for i, text in enumerate(category_items, start=1):
            self.assert_text(text, f".sidebar-widget li:nth-child({i})")
        # verify that the categories on the left side of the screen are listed on the page
