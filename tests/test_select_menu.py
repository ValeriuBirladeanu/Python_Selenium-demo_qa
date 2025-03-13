import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Widgets")
class TestSelectMenu(BaseTest):
    @allure.title("Test value dropdown")
    @pytest.mark.smoke
    @pytest.mark.screenshot
    def test_select_value_dropdown(self):
        self.select_menu.open()
        self.select_menu.is_opened()
        self.select_menu.select_value_option()

    @allure.title("Test one dropdown")
    @pytest.mark.smoke
    @pytest.mark.screenshot
    def test_select_one_dropdown(self):
        self.select_menu.open()
        self.select_menu.is_opened()
        self.select_menu.select_one_option()

    @allure.title("Test old style dropdown")
    @pytest.mark.smoke
    @pytest.mark.screenshot
    def test_select_old_style_dropdown(self):
        self.select_menu.open()
        self.select_menu.is_opened()
        self.select_menu.select_old_style_menu_option()

    @allure.title("Test multiselect dropdown")
    @pytest.mark.smoke
    @pytest.mark.screenshot
    def test_multiselect_dropdown(self):
        self.select_menu.open()
        self.select_menu.is_opened()
        self.select_menu.select_multiselect_dropdown()

    @allure.title("Test standard multiselect dropdown")
    @pytest.mark.smoke
    @pytest.mark.screenshot
    def test_standard_multiselect_dropdown(self):
        self.select_menu.open()
        self.select_menu.is_opened()
        self.select_menu.select_standard_multiselect_dropdown()