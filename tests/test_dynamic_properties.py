import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Elements - Dynamic Properties")
class TestDynamicProperties(BaseTest):

    @allure.title("Test enable button")
    @pytest.mark.smoke
    def test_enable_button(self):
        self.dynamic_properties.open()
        self.dynamic_properties.is_opened()
        self.dynamic_properties.check_enable_button()
        self.dynamic_properties.make_screenshot()

    @allure.title("Test change color")
    @pytest.mark.smoke
    def test_change_button_color_change(self):
        self.dynamic_properties.open()
        self.dynamic_properties.is_opened()
        self.dynamic_properties.check_button_color_change()
        self.dynamic_properties.make_screenshot()

    @allure.title("Test appearance button")
    @pytest.mark.smoke
    def test_appearance_button(self):
        self.dynamic_properties.open()
        self.dynamic_properties.is_opened()
        self.dynamic_properties.check_appearance_button()
        self.dynamic_properties.make_screenshot()