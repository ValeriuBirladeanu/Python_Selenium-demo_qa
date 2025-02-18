import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Widgets")
class TestSlider(BaseTest):
    @allure.title("Test slider")
    @pytest.mark.smoke
    @pytest.mark.screenshot
    def test_slider(self):
        self.slider.open()
        self.slider.is_opened()
        self.slider.change_slider_value()
        self.slider.check_slider_value_change()