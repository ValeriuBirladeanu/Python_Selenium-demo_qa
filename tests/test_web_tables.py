import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Elements - Wev Tables")
class TestWebTables(BaseTest):

    @allure.title("Add new person in web tables")
    @pytest.mark.smoke
    def test_add_new_person(self):
        self.web_tables.open()
        self.web_tables.is_opened()
        self.web_tables.click_add()
        self.web_tables.check_open_modal_window()
        self.web_tables.enter_first_name()
        self.web_tables.enter_last_name()
        self.web_tables.enter_email()
        self.web_tables.enter_age()
        self.web_tables.enter_salary()
        self.web_tables.enter_department()
        self.web_tables.make_screenshot()
        self.web_tables.check_values_in_input_fields()
        self.web_tables.click_submit()
        self.web_tables.make_screenshot()
        self.web_tables.verify_text_in_table_entries()

    @allure.title("Search person in web tables")
    @pytest.mark.smoke
    def test_search_some_person(self):
        self.web_tables.open()
        self.web_tables.is_opened()
        self.web_tables.search_some_person()
        self.web_tables.check_search_person()
        self.web_tables.make_screenshot()

    @allure.title("Edit person from web tables")
    @pytest.mark.smoke
    def test_edit_some_person(self):
        self.web_tables.open()
        self.web_tables.is_opened()
        self.web_tables.make_screenshot()
        self.web_tables.edit_some_person()
        self.web_tables.make_screenshot()

    @allure.title("Delete a random person and verify deletion")
    @pytest.mark.smoke
    def test_delete_person(self):
        self.web_tables.open()
        self.web_tables.is_opened()
        self.web_tables.make_screenshot()
        self.web_tables.delete_person_from_table()
        self.web_tables.verify_deleted_person_from_table()
        self.web_tables.make_screenshot()