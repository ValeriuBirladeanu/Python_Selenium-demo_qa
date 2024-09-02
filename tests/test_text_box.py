import allure
import pytest
from base.base_test import BaseTest

@allure.feature("Elements - Text Box")
class TestTextBox(BaseTest):

    @allure.title("Completing the text box fields")
    # @pytest.mark.smoke
    def test_complete_text_box(self):
        self.text_box.open()
        self.text_box.is_opened()
        self.text_box.enter_full_name()
        self.text_box.enter_email()
        self.text_box.enter_current_address()
        self.text_box.enter_permanent_address()
        self.text_box.click_submit()
        self.text_box.is_saved_full_name()
        self.text_box.is_saved_email()
        self.text_box.is_saved_current_address()
        self.text_box.is_saved_permanent_address()
        self.text_box.make_screenshot("ScreenShot")
