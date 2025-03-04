import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Widgets")
class TestMenu(BaseTest):
    @allure.title("Test Menu")
    @pytest.mark.smoke
    @pytest.mark.screenshot
    def test_menu(self):
        self.menu.open()
        self.menu.is_opened()
        self.menu.receiving_names_of_all_menus()
        self.menu.check_menu_names()