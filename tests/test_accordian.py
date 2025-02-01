import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Widgets")
class TestAccordian(BaseTest):
    @allure.title("Test accordian")
    @pytest.mark.smoke
    @pytest.mark.screenshot
    def test_accordian(self):
        self.accordian.open()
        self.accordian.is_opened()
        self.accordian.select_accordian()
        self.accordian.check_open_new_accordian()