import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Widgets")
class TestTabs(BaseTest):
    @allure.title("Test tabs")
    @pytest.mark.smoke
    @pytest.mark.screenshot
    def test_tabs(self, ):
        self.tabs.open()
        self.tabs.is_opened()
        self.tabs.select_another_tab()
        self.tabs.check_open_new_tab()