import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Widgets")
class TestAutoComplete(BaseTest):
    @allure.title("Test multiple names input")
    @pytest.mark.smoke
    def test_multiple_names_input(self):
        self.auto_complete.open()
        self.auto_complete.is_opened()
        self.auto_complete.choose_multiple_names_input()
        self.auto_complete.check_completed_multiple_names_input()
        self.auto_complete.make_screenshot()

    @allure.title("Test single name input")
    @pytest.mark.smoke
    def test_single_name_input(self):
        self.auto_complete.open()
        self.auto_complete.is_opened()
        self.auto_complete.choose_single_name_input()
        self.auto_complete.check_completed_single_name_input()
        self.auto_complete.make_screenshot()