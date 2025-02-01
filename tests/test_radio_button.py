import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Elements - Radio Button")
class TestRadioButton(BaseTest):

    @allure.title("Select and verify a random radio button")
    @pytest.mark.smoke
    @pytest.mark.screenshot
    def test_random_radio_button(self):
        self.radio_button.open()
        self.radio_button.is_opened()
        self.radio_button.click_random_radio_button_and_verify()

    @allure.title("Verify 'No' radio button is disabled")
    @pytest.mark.smoke
    @pytest.mark.screenshot
    def test_disabled_radio_button(self):
        self.radio_button.open()
        self.radio_button.is_opened()
        self.radio_button.check_if_no_radio_button_is_disabled()