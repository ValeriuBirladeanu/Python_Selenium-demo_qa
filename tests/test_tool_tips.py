import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Widgets")
class TestToolTips(BaseTest):
    @allure.title("Test tool tips")
    @pytest.mark.smoke
    @pytest.mark.screenshot
    def test_tool_tips(self):
        self.tool_tips.open()
        self.tool_tips.is_opened()
        self.tool_tips.check_tooltip_button()
        self.tool_tips.check_tooltip_input()
        self.tool_tips.check_tooltip_text_contrary()
        self.tool_tips.check_tooltip_text_1_10_32()