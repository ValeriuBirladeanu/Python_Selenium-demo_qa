import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Elements - Buttons")
class TestButtons(BaseTest):

    @allure.title("Double click")
    @pytest.mark.smoke
    @pytest.mark.screenshot
    def test_click_double_button(self):
        self.buttons.open()
        self.buttons.is_opened()
        self.buttons.double_click()
        self.buttons.check_double_click()

    @allure.title("Right click")
    @pytest.mark.smoke
    @pytest.mark.screenshot
    def test_click_right_button(self):
        self.buttons.open()
        self.buttons.is_opened()
        self.buttons.right_click()
        self.buttons.check_right_click()

    @allure.title("A click")
    @pytest.mark.smoke
    @pytest.mark.screenshot
    def test_click_button(self):
        self.buttons.open()
        self.buttons.is_opened()
        self.buttons.click()
        self.buttons.check_a_click()