from seleniumbase import BaseCase

class TestContactPage(BaseCase):

    # Positive Assertions

    def test_sent_message(self):
        self.open('https://practice-react.sdetunicorns.com/contact')
        self.click('.col-lg-6')
        self.type('[placeholder="Name*"]', 'test')
        self.click('.col-lg-6')
        self.type('[placeholder="Email*"]', 'test@email.com')
        self.click('.col-lg-12')
        self.type('[placeholder="Subject*"]', 'test subject')
        self.click('.col-lg-12')
        self.type('[placeholder="Your Message*"]', 'test message')
        self.click('.submit')
        # self.assert_element_visible('.react-toast-notifications__container') # It looks like this element is always present and the sent message disappears after it shows
        self.assert_text('Message sent successfully', ".react-toast-notifications__toast__content" )
    def test_error_message_name(self):
        self.open('https://practice-react.sdetunicorns.com/contact')
        self.click('.submit')
        self.assert_element_visible('[class*=error]')

    def test_number_of_errors(self):
        self.open('https://practice-react.sdetunicorns.com/contact')
        self.click('.submit')
        errors_el = self.find_elements('[class*=error]')
        self.assert_true(len(errors_el) == 4)



    # Negative Assertions

    def test_submit_not_visible(self):
        self.open('https://practice-react.sdetunicorns.com/contact')
        self.click('.submit')
        self.assert_false(self.is_text_visible('Email is optional', '.error-email'))
        error_message = self.get_text('.error-message')
        self.assert_in('Message', error_message)
        self.assert_element_not_present('.react-toast-notifications__content')

    #.react-toast-notifications__toast__content <- this is what shows when the sent message pops up

    def test_email_subscribe_not_sent(self):
        self.open('https://practice-react.sdetunicorns.com/contact')
        self.click('.button')
        self.assert_element_not_visible('color: rgb(52, 152, 219); font-size: 12px;')

    def test_error_message_not_visible(self):
        self.open('https://practice-react.sdetunicorns.com/contact')
        self.click('.col-lg-6')
        self.type('[placeholder="Name*"]', 'test')
        self.click('.col-lg-6')
        self.type('[placeholder="Email*"]', 'test@email.com')
        self.click('.col-lg-12')
        self.type('[placeholder="Subject*"]', 'test subject')
        self.click('.col-lg-12')
        self.type('[placeholder="Your Message*"]', 'test message')
        self.click('.submit')
        self.assert_element_not_visible('[class*=error]')




