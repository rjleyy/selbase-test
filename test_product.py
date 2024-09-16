from seleniumbase import BaseCase

class TestProductsPage(BaseCase):

    def test_add_to_cart_implicit_wait(self):
        self.open('https://practice-react.sdetunicorns.com/product/63448f0500b2931578c0a5a5')
        self.driver.implicitly_wait(10)
        self.driver.find_element(by='css selector', value= '.pro-details-cart')
        self.click('.pro-details-cart')
        self.assert_text('Added To Cart', '.react-toast-notifications__toast__content')

    def test_add_to_cart_explicit_wait(self):
        self.open('https://practice-react.sdetunicorns.com/product/63448f0500b2931578c0a5a5')
        self.click('.pro-details-carts', timeout=2) # explicit timeout