import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Forms - Practice Form")
class TestPracticeForm(BaseTest):

    @allure.title("Complete practice form")
    @pytest.mark.smoke
    @pytest.mark.screenshot
    def test_complete_form(self):
        self.practice_form.open()
        self.practice_form.is_opened()
        self.practice_form.enter_first_name()
        self.practice_form.enter_last_name()
        self.practice_form.enter_email()
        self.practice_form.choose_random_radio_button_gender()
        self.practice_form.enter_mobile_number()
        self.practice_form.complete_calendar()
        self.practice_form.choose_subjects()
        self.practice_form.choose_random_checkboxes_hobbies()
        self.practice_form.enter_current_address()
        self.practice_form.select_state()
        self.practice_form.select_city()
        self.practice_form.click_submit()
        self.practice_form.check_present_corrected_data_in_table()