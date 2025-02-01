import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Elements - Check Box")
class TestCheckBox(BaseTest):

    @allure.title("Click on the checkboxes")
    @pytest.mark.smoke
    @pytest.mark.screenshot
    def test_click_check_box(self):
        self.check_box.open()
        self.check_box.is_opened()
        self.check_box.click_expand_all()
        self.check_box.verify_checkboxes_visible_and_clickable()
        self.check_box.click_random_checkbox()
        self.check_box.verify_checkbox_selections()