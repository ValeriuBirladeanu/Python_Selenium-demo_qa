import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Elements - Dynamic Properties")
class TestDynamicProperties(BaseTest):

    @allure.title("Test enable button")
    @pytest.mark.smoke
    @pytest.mark.screenshot
    def test_enable_button(self):
        self.dynamic_properties.open()
        self.dynamic_properties.is_opened()
        self.dynamic_properties.check_enable_button()

    @allure.title("Test change color")
    @pytest.mark.smoke
    @pytest.mark.screenshot
    def test_change_button_color_change(self):
        self.dynamic_properties.open()
        self.dynamic_properties.is_opened()
        self.dynamic_properties.check_button_color_change()

    @allure.title("Test appearance button")
    @pytest.mark.smoke
    @pytest.mark.screenshot
    def test_appearance_button(self):
        self.dynamic_properties.open()
        self.dynamic_properties.is_opened()
        self.dynamic_properties.check_appearance_button()