from seleniumbase import BaseCase

class TestDemoPage(BaseCase):

    def test_input_slider(self):

        # Before State
        self.open('https://seleniumbase.io/demo_page')
        # Establish a before State
        self.assert_attribute('#progressBar', 'value', '50' )
        # Change the slider value
        self.set_value('#mySlider', '80')
        # Check the after state
        self.assert_attribute('#progressBar', 'value', '80')

    def test_drop_down_list(self):
        self.open('https://seleniumbase.io/demo_page')
        # Assert the value of the before state
        self.assert_attribute('#meterBar', 'value', '0.25' )
        # Click on the dropdown menu
        self.click('#mySelect')
        # Select the dropdown selector and the option you want
        self.select_option_by_value('.selectClass', '75%')
        # Check the value of the bar again
        self.assert_attribute('#meterBar', 'value', '0.75')

    def test_checklist(self):
        self.open('https://seleniumbase.io/demo_page')
        # ensure the logo is not visible on the checkbox
        self.assert_element_not_visible('img#logo')
        # check if the checkbox is selected
        self.assert_false(self.is_selected('#checkbox1'))
        #check checkbox
        self.click('#checkbox1')
        # Check that it is selected
        self.assert_true(self.is_selected('#checkbox1'))
        # check if the logo is visible
        self.assert_element_visible('img#logo')

    def test_iFrame(self):
        self.open('https://seleniumbase.io/demo_page')
        # Check to see that the element within the iFrame cannot be seen
        self.assert_element_not_visible('h4')
        # Switch over to iFrame
        self.switch_to_frame('#myFrame2')
        # Check back on the header that was within the iFrame
        self.assert_element_present('h4')
        self.assert_text('iFrame Text', 'h4')
        # You can also go back to the original root content
        self.switch_to_default_content()
        # Assert something in the root domain
        self.assert_element('#progressBar')
    def test_iFrame_checkbox(self):
        self.open('https://seleniumbase.io/demo_page')
        self.assert_element_not_visible('#checkBox6')
        self.switch_to_frame('#myFrame3')
        self.click('#checkBox6')
        self.switch_to_default_content()
        self.assert_element('#progressBar')
    def test_hover_dropdown(self):
        self.open('https://seleniumbase.io/demo_page')
        # Hover over the dropdown element
        ## self.hover('#myDropdown')
        # Click on the option
        ## self.click('#dropOption2')
        # We can also perform a hover and Click
        self.hover_and_click('#myDropdown', '#dropOption2')
        # Assert that the option has updated
        self.assert_text('Link Two Selected', 'h3')






