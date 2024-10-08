import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Forms - Practice Form")
class TestPracticeForm(BaseTest):

    @allure.title("Complete form")
    @pytest.mark.smoke
    def test_complete_form(self):
        self.practice_form.open()
        self.practice_form.is_opened()
        self.practice_form.enter_first_name()
        self.practice_form.enter_last_name()
        self.practice_form.enter_email()
        self.practice_form.click_random_radio_button()
        self.practice_form.enter_mobile_number()
        self.practice_form.complete_calendar()
        self.practice_form.select_subjects()
        self.practice_form.click_random_checkboxes_hobbies()
        self.practice_form.enter_current_address()
        self.practice_form.select_state()
        self.practice_form.select_city()
        self.practice_form.click_submit()