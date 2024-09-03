import allure
import pytest
from base.base_test import BaseTest

@allure.feature("Elements - Check Box")
class TestCheckBox(BaseTest):

    @allure.title("Click on the checkboxes")
    @pytest.mark.smoke
    def test_click_check_box(self):
        self.check_box.open()
        self.check_box.is_opened()
        self.check_box.click_expand_all()
        self.check_box.click_random_checkbox()
        input_result = self.check_box.get_checked_checkboxes()
        output_result = self.check_box.get_output_results()
        assert input_result == output_result,  f"Mismatch between input and output results: {input_result} != {output_result}"
        self.check_box.make_screenshot()