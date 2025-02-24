import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Widgets")
class Test_Progress_Bar(BaseTest):
    @allure.title("Test progress bar with random delay between clicks")
    @pytest.mark.smoke
    @pytest.mark.screenshot
    def test_progress_bar_single_click_with_delay(self):
        self.progress_bar.open()
        self.progress_bar.is_opened()
        self.progress_bar.change_progress_bar_value()
        self.progress_bar.check_progres_bar_value_change()

    @allure.title("Test progress bar with multiple clicks")
    @pytest.mark.smoke
    @pytest.mark.screenshot
    def test_progress_bar_multiple_clicks(self):
        self.progress_bar.open()
        self.progress_bar.is_opened()
        self.progress_bar.change_progress_bar_value_multiple_clicks()
        self.progress_bar.check_progres_bar_value_change()